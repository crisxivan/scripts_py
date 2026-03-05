import json
import requests
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import get_headers

import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

api_url = "http://localhost:58001/api/v1/network-device"

headers = get_headers()
logging.info(f"Headers: {headers}")

logging.info(f"GET {api_url}")
resp = requests.get(api_url, headers=headers)

print("Status: ", resp.status_code)
response_json = resp.json()
print(response_json)
