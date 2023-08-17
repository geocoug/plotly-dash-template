#!/usr/bin/env python

import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

APP_DIR = Path(__file__).parent
os.environ["APP_DIR"] = APP_DIR.as_posix()

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, APP_DIR.as_posix())

load_dotenv(Path(APP_DIR.as_posix(), ".env"))

from web.app import dashboard as application  # noqa
