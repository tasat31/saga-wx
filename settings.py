import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging

load_dotenv()
MY_STATIONS = os.environ.get("MY_STATIONS")
AIS_JAPAN_USER = os.environ.get("AIS_JAPAN_USER")
AIS_JAPAN_PASSWORD = os.environ.get("AIS_JAPAN_PASSWORD")

