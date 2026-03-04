import json
import requests
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import get_headers

import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

api_url = "http://172.28.32.1:58000/api/v1/network-device"

headers = get_headers()
logging.info(f"Headers: {headers}")

body_json = {
    "ipAddress": "172.21.80.254",
    "globalCredentialId": "c8cd2f4b-e446-4712-b51d-d01c5ba3058e"
}

logging.info(f"PUT {api_url}")
resp = requests.put(api_url, json.dumps(body_json), headers=headers)

print("Status: ", resp.status_code)
response_json = resp.json()
print(response_json)
