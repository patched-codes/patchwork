from __future__ import annotations

import functools
import hashlib
import logging
import uuid

from pydantic import BaseModel

from patchwork.managed_files import CONFIG_FILE


class UserConfig(BaseModel):
    id: str = hashlib.sha256(str(uuid.getnode()).encode()).hexdigest()

    def persist(self):
        try:
            CONFIG_FILE.write_text(self.json())
        except Exception as e:
            logging.error(f"Failed to persist user config: {e}")

    @staticmethod
    def read() -> 'UserConfig' | None:
        try:
            return UserConfig.model_validate_strings(CONFIG_FILE.read_text())
        except Exception as e:
            logging.error(f"Failed to read user config: {e}")
            return None


@functools.lru_cache(maxsize=None)
def get_user_config():
    user_config = UserConfig.read()
    if user_config is not None:
        return user_config

    user_config = UserConfig()
    user_config.persist()
    return user_config
