"""Utility helpers used by the various endpoint scripts."""

import logging
import os
from typing import Dict

from auth.generate_token import get_token

# very simple console logging
logging.basicConfig(level=logging.INFO, format="%(message)s")


def get_headers(token: str | None = None) -> Dict[str, str]:
    if token:
        logging.info("Using explicit token provided")
        t = token
    else:
        t = os.environ.get("DNAC_TOKEN")
        if t:
            logging.info("Using token from DNAC_TOKEN environment variable")
        else:
            logging.info("No existing token found; obtaining a new one")
            t = get_token()
    return {"X-Auth-Token": t, "Content-Type": "application/json"}
