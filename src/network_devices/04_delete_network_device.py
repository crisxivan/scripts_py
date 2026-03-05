import json
import requests
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import get_headers

import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

device_id = "FDO1302M5F7-uuid"
api_url = f"http://localhost:58001/api/v1/network-device/{device_id}"

headers = get_headers()
logging.info(f"Headers: {headers}")

logging.info(f"DELETE {api_url}")
resp = requests.delete(api_url, headers=headers)

print("Status: ", resp.status_code)
print(resp.text)
