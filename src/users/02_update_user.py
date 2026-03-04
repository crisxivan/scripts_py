import json
import requests
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import get_headers

import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

api_url = "http://172.28.32.1:58000/api/v1/user"

headers = get_headers()
logging.info(f"Headers: {headers}")

body_json = {
    "username": "admin1",
    "oldPassword": "cisco!!!",
    "password": "cisco",
    "authorization": [
        {
            "role": "ROLE_OBSERVER"
        }
    ]
}

logging.info(f"PUT {api_url}")
resp = requests.put(api_url, json.dumps(body_json), headers=headers)

print("Status: ", resp.status_code)
response_json = resp.json()
print(response_json)
