
from typing import Final

from dotenv import load_dotenv
import os

import logging

load_dotenv()

DB_HOST: Final = os.getenv("DB_HOST")
DB_USER: Final = os.getenv("DB_USER")
DB_NAME: Final = os.getenv("DB_NAME")
DB_PASS: Final = os.getenv("DB_PASS")
DB_PORT: Final = os.getenv("DB_PORT")

DB_URL: Final = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

APP_NAME = "Labs"


def configure_logging(level: int = logging.INFO) -> None:
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="%(levelname)-9s %(message)r %(funcName)s() in <%(module)s:%(lineno)3d> at [%(asctime)s.%(msecs)03d]"
    )