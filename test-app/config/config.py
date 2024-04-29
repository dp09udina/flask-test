import json
from pathlib import Path
from typing import Dict


class Config:
    LOGGING_LEVEL: str = "INFO"
    CONFIG_PATH: Path
    CONFIG: Dict = {}

    @classmethod
    def read_config(cls, config_filepath):
        with open(config_filepath, "r", encoding="UTF-8") as config:
            cls.CONFIG = json.load(config)
        if cls.CONFIG.get("debug"):
            cls.LOGGING_LEVEL = "DEBUG"
        cls.CONFIG_PATH = Path(config_filepath)


# config_filepath = Path("test-app/config/config.json").resolve()
config_filepath = Path("config/config.json").resolve()
if not config_filepath.is_file():
    raise FileNotFoundError(f"{config_filepath} does't not found!")
Config.read_config(config_filepath)
