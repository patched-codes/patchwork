import atexit
import contextlib
import os
import pathlib
import socket
import sys
from typing import List

import click
import requests
from git.repo.base import Repo
from requests import Response, Session
from requests.adapters import DEFAULT_POOLBLOCK, HTTPAdapter
from urllib3 import HTTPConnectionPool, HTTPSConnectionPool, PoolManager
from pydantic import BaseModel

from patchwork.common.utils import get_current_branch
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

    @contextlib.contextmanager
    def patched_telemetry(self, patchflow: str, repo: Repo, inputs: dict):
        try:
            is_valid_client = self.test_token()
        except Exception as e:
            logger.error(f"Access Token test failed: {e}")
            yield
            return

        if not is_valid_client:
            yield
            return

        try:
            patchflow_run_id = self.record_patchflow_run(patchflow, repo, inputs)
        except Exception as e:
            logger.error(f"Failed to record patchflow run: {e}")
            yield
            return

        if patchflow_run_id is None:
            yield
            return

        try:
            yield
        finally:
            try:
                self.finish_record_patchflow_run(patchflow_run_id, patchflow, repo)
            except Exception as e:
                logger.error(f"Failed to finish patchflow run: {e}")

    def record_patchflow_run(self, patchflow: str, repo: Repo, inputs: dict) -> int | None:
        head = get_current_branch(repo)
        branch = head.remote_head if head.is_remote() else head.name

        response = self._post(
            url=self.url + "/v1/patchwork/",
            headers={"Authorization": f"Bearer {self.access_token}"},
            json={
                "url": repo.remotes.origin.url,
                "patchflow": patchflow,
                "branch": branch,
                "inputs": inputs
            }
        )

        if response is None:
            return None

        if not response.ok:
            logger.error(f"Failed to record patchflow run with status code {response.status_code}, msg:{response.text}")
            return None

        logger.info(f"Patchflow run recorded for {patchflow}")
        return response.json()["id"]

    def finish_record_patchflow_run(self, id: int, patchflow: str, repo: Repo) -> None:
        response = self._post(
            url=self.url + "/v1/patchwork/",
            headers={"Authorization": f"Bearer {self.access_token}"},
            json={
                "id": id,
                "url": repo.remotes.origin.url,
                "patchflow": patchflow,
            }
        )

        if response is None:
            return

        if not response.ok:
            logger.error(f"Failed to finish patchflow run with status code {response.status_code}, msg:{response.text}")
            return

        logger.info(f"Patchflow run finished for {id}")