import json
import requests
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import get_headers

import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

username = "admin1"
api_url = f"http://172.28.32.1:58000/api/v1/user/{username}"

headers = get_headers()
logging.info(f"Headers: {headers}")

logging.info(f"GET {api_url}")
resp = requests.get(api_url, headers=headers)

print("Status: ", resp.status_code)
response_json = resp.json()
print(response_json)
