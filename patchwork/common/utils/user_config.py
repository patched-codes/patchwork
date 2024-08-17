from __future__ import annotations

import functools
import hashlib
import uuid

from pydantic import BaseModel

from patchwork.logger import logger
from patchwork.managed_files import CONFIG_FILE


class __UserConfig(BaseModel):
    id: str = hashlib.sha256(str(uuid.getnode()).encode()).hexdigest()

    def persist(self):
        try:
            CONFIG_FILE.write_text(self.model_dump_json())
        except Exception as e:
            logger.debug(f"Failed to persist user config: {e}")


@functools.lru_cache(maxsize=None)
def get_user_config():
    try:
        return __UserConfig.model_validate_json(CONFIG_FILE.read_text())
    except Exception as e:
        logger.debug(f"Failed to read user config: {e}")

    user_config = __UserConfig()
    user_config.persist()
    return user_config
