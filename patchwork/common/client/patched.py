from __future__ import annotations

import asyncio
import atexit
import contextlib
import platform
import socket
import sys
from importlib import metadata
from pathlib import Path
from threading import Thread

import click
import requests
from git.repo.base import Repo
from requests import Response, Session
from requests.adapters import DEFAULT_POOLBLOCK, HTTPAdapter
from typing_extensions import Any
from urllib3 import HTTPConnectionPool, HTTPSConnectionPool, PoolManager

from patchwork.common.utils.user_config import get_user_config
from patchwork.common.utils.utils import get_current_branch, is_container
from patchwork.logger import logger


class TCPKeepAliveHTTPSConnectionPool(HTTPSConnectionPool):
    # probe start
    TCP_KEEP_IDLE = 60
    # probe interval
    TCP_KEEPALIVE_INTERVAL = 60
    # probe times
    TCP_KEEP_CNT = 3

    def _validate_conn(self, conn):
        super()._validate_conn(conn)

        if sys.platform == "linux":
            if hasattr(socket, "TCP_KEEPIDLE"):
                conn.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, self.TCP_KEEP_IDLE)
            if hasattr(socket, "TCP_KEEPINTVL"):
                conn.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, self.TCP_KEEPALIVE_INTERVAL)
            if hasattr(socket, "TCP_KEEPCNT"):
                conn.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, self.TCP_KEEP_CNT)
        elif sys.platform == "darwin":
            conn.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            conn.sock.setsockopt(socket.IPPROTO_TCP, 0x10, self.TCP_KEEPALIVE_INTERVAL)
        elif sys.platform == "win32":
            conn.sock.ioctl(
                socket.SIO_KEEPALIVE_VALS, (1, self.TCP_KEEP_IDLE * 1000, self.TCP_KEEPALIVE_INTERVAL * 1000)
            )


class KeepAlivePoolManager(PoolManager):
    def __init__(self, num_pools=10, headers=None, **connection_pool_kw):
        super().__init__(num_pools=num_pools, headers=headers, **connection_pool_kw)
        self.pool_classes_by_scheme = {
            "http": HTTPConnectionPool,
            "https": TCPKeepAliveHTTPSConnectionPool,
        }


class KeepAliveHTTPSAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=DEFAULT_POOLBLOCK, **pool_kwargs):
        self.poolmanager = KeepAlivePoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            strict=True,
            **pool_kwargs,
        )


class PatchedClient(click.ParamType):
    TOKEN_URL = "https://app.patched.codes/signin"
    DEFAULT_PATCH_URL = "https://patchwork.patched.codes"
    ALLOWED_TELEMETRY_KEYS = {
        "model",
    }
    ALLOWED_TELEMETRY_OUTPUT_KEYS = {
        "pr_url",
        "issue_url",
    }

    def __init__(self, access_token: str, url: str = DEFAULT_PATCH_URL):
        self.access_token = access_token
        self.url = url
        self._session = Session()
        atexit.register(self._session.close)
        self._edit_tcp_alive()

    def _edit_tcp_alive(self):
        # credits to https://www.finbourne.com/blog/the-mysterious-hanging-client-tcp-keep-alives
        self._session.mount("https://", KeepAliveHTTPSAdapter())

    def _post(self, **kwargs) -> Response | None:
        try:
            response = self._session.post(**kwargs)
        except requests.ConnectionError as e:
            logger.error(f"Unable to establish connection to patched server: {e}")
            return None
        except requests.RequestException as e:
            logger.error(f"Request failed with exception: {e}")
            return None

        return response

    def _get(self, **kwargs) -> Response | None:
        try:
            response = self._session.get(**kwargs)
        except requests.ConnectionError as e:
            logger.error(f"Unable to establish connection to patched server: {e}")
            return None
        except requests.RequestException as e:
            logger.error(f"Request failed with exception: {e}")
            return None

        return response

    def test_token(self) -> bool:
        response = self._post(
            url=self.url + "/token/test", headers={"Authorization": f"Bearer {self.access_token}"}, json={}
        )

        if response is None:
            return False

        if not response.ok:
            logger.error(f"Access Token failed with status code {response.status_code}")
            return False

        body = response.json()
        if "msg" not in body:
            logger.error("Access Token test failed with unknown response")
            return False

        return body["msg"] == "ok"

    def __handle_telemetry_inputs(self, inputs: dict[str, Any]) -> dict:
        diff_keys = set(inputs.keys()).difference(self.ALLOWED_TELEMETRY_KEYS)

        inputs_copy = inputs.copy()
        for key in diff_keys:
            inputs_copy[key] = True

        return inputs_copy

    def __handle_telemetry_outputs(self, outputs: dict[str, Any]) -> dict:
        diff_keys = set(outputs.keys()).difference(self.ALLOWED_TELEMETRY_OUTPUT_KEYS)

        outputs_copy = outputs.copy()
        for key in diff_keys:
            del outputs_copy[key]

        return outputs_copy

    async def _public_telemetry(self, patchflow: str, inputs: dict[str, Any]):
        user_config = get_user_config()
        requests.post(
            url=self.url + "/v1/telemetry/",
            headers={"Authorization": f"Bearer {self.access_token}"},
            json=dict(
                client_id=user_config.id,
                patchflow=patchflow,
                inputs=self.__handle_telemetry_inputs(inputs),
                environment=dict(
                    system=platform.system(),
                    release=platform.release(),
                    machine=platform.machine(),
                    python_version=platform.python_version(),
                    cli_version=metadata.version("patchwork-cli"),
                    is_container=is_container(),
                ),
            ),
        )

    def send_public_telemetry(self, patchflow: str, inputs: dict):
        try:
            _thread = Thread(target=asyncio.run, args=(self._public_telemetry(patchflow, inputs),))
            _thread.start()
        except Exception as e:
            logger.debug(f"Failed to send public telemetry: {e}")

    @contextlib.contextmanager
    def patched_telemetry(self, patchflow: str, inputs: dict):
        outputs = dict()

        if not self.access_token:
            yield outputs
            return

        try:
            is_valid_client = self.test_token()
        except Exception as e:
            logger.error(f"Access Token test failed: {e}")
            yield outputs
            return

        if not is_valid_client:
            yield outputs
            return

        try:
            repo = Repo(Path.cwd(), search_parent_directories=True)
            patchflow_run_id = self.record_patchflow_run(patchflow, repo, self.__handle_telemetry_inputs(inputs))
        except Exception as e:
            logger.error(f"Failed to record patchflow run: {e}")
            yield outputs
            return

        if patchflow_run_id is None:
            yield outputs
            return

        try:
            yield outputs
        finally:
            try:
                self.finish_record_patchflow_run(
                    patchflow_run_id, patchflow, repo, self.__handle_telemetry_outputs(outputs)
                )
            except Exception as e:
                logger.error(f"Failed to finish patchflow run: {e}")

    def record_patchflow_run(self, patchflow: str, repo: Repo, inputs: dict) -> int | None:
        head = get_current_branch(repo)
        branch = head.remote_head if head.is_remote() else head.name

        response = self._post(
            url=self.url + "/v1/patchwork/",
            headers={"Authorization": f"Bearer {self.access_token}"},
            json={"url": repo.remotes.origin.url, "patchflow": patchflow, "branch": branch, "inputs": inputs},
        )

        if response is None:
            return None

        if not response.ok:
            logger.error(f"Failed to record patchflow run with status code {response.status_code}, msg:{response.text}")
            return None

        logger.debug(f"Patchflow run recorded for {patchflow}")
        return response.json().get("id")

    def finish_record_patchflow_run(self, id: int, patchflow: str, repo: Repo, outputs: dict) -> None:
        response = self._post(
            url=self.url + "/v1/patchwork/",
            headers={"Authorization": f"Bearer {self.access_token}"},
            json={"id": id, "url": repo.remotes.origin.url, "patchflow": patchflow, "outputs": outputs},
        )

        if response is None:
            return

        if not response.ok:
            logger.error(f"Failed to finish patchflow run with status code {response.status_code}, msg:{response.text}")
            return

        logger.debug(f"Patchflow run finished for {id}")
