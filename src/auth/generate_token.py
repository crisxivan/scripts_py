import json
import os
import argparse
import logging
import requests

# configure simple logging to console
logging.basicConfig(level=logging.INFO, format="%(message)s")

# ----- configuration defaults ------------------------------------------------
DEFAULT_BASE_URL = os.environ.get("DNA_CENTER_URL", "http://localhost:58001")
DEFAULT_USERNAME = os.environ.get("DNA_CENTER_USER", "admin")
DEFAULT_PASSWORD = os.environ.get("DNA_CENTER_PASS", "cisco!")

# ---------------------------------------------------------------------------

def get_token(base_url: str = DEFAULT_BASE_URL,
              username: str = DEFAULT_USERNAME,
              password: str = DEFAULT_PASSWORD) -> str:
    logging.info(f"Requesting service ticket from {base_url}")
    api_url = f"{base_url}/api/v1/ticket"
    headers = {"Content-Type": "application/json"}
    body = {"username": username, "password": password}

    resp = requests.post(api_url, json.dumps(body), headers=headers)
    resp.raise_for_status()
    data = resp.json()
    ticket = data["response"]["serviceTicket"]
    logging.info("Received service ticket")
    return ticket


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print DNA Center service ticket")
    parser.add_argument("--url", help="Base URL of the controller",
                        default=DEFAULT_BASE_URL)
    parser.add_argument("--user", help="Username for authentication",
                        default=DEFAULT_USERNAME)
    parser.add_argument("--pass", dest="password",
                        help="Password for authentication",
                        default=DEFAULT_PASSWORD)
    args = parser.parse_args()

    try:
        ticket = get_token(args.url, args.user, args.password)
        print(ticket)
    except Exception as e:
        parser.error(f"failed to obtain token: {e}")
