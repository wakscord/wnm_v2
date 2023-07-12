import os
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from dotenv import dotenv_values

env_path = Path.joinpath(Path(__file__).parent.parent.parent.resolve(), ".env")
if not os.path.exists(env_path):
    raise Exception("Dotenv is not exists.")

raw_settings = dotenv_values(env_path)


@dataclass(frozen=True)
class Settings:
    REDIS_URL: str
    REDIS_PORT: int
    REDIS_PASSWORD: str | None = None
    API_KEY: str = "wakscord"


to_int: Callable[[str, int], int] = lambda value, else_value: int(value) if value else else_value

settings = Settings(
    REDIS_URL=raw_settings.get("REDIS_URL") or "localhost",
    REDIS_PORT=to_int(raw_settings.get("REDIS_PORT"), 6379),
    REDIS_PASSWORD=raw_settings.get("REDIS_PASSWORD"),
)
