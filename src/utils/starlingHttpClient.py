import httpx
import os
import logging
from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

BASE_URL = os.getenv('BASE_URL') #to access sandbox accounts: https://api-sandbox.starlingbank.com


def get_headers():
    access_token = os.getenv('STARLING_ACCESS_TOKEN')
    if not access_token:
        logger.error("STARLING_ACCESS_TOKEN is not set.")
        raise ValueError("Missing access token.")
    return {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

def get_request(endpoint):
    url = f"{BASE_URL}{endpoint}"
    with httpx.Client() as client:
        response = client.get(url, headers=get_headers())
        response.raise_for_status()
        return response

def post_request(endpoint, data):
    url = f"{BASE_URL}{endpoint}"
    with httpx.Client() as client:
        response = client.post(url, headers=get_headers(), json=data)
        response.raise_for_status()
        return response

