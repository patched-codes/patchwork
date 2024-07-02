import hashlib
import uuid
from functools import lru_cache

from pydantic import BaseModel

from patchwork.managed_files import CONFIG_FILE


class UserConfig(BaseModel):
    id: str = hashlib.sha256(str(uuid.getnode()).encode()).hexdigest()

    def persist(self):
        CONFIG_FILE.write_text(self.json())

    @staticmethod
    def read():
        return UserConfig.model_validate_strings(CONFIG_FILE.read_text())


@lru_cache(maxsize=None)
def get_user_config():
    try:
        return UserConfig.read()
    except Exception:
        pass

    user_config = UserConfig()
    user_config.persist()
    return user_config
