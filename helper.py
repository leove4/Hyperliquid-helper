import requests
from datetime import datetime, timezone


BASE_URL = "https://api.hyperliquid.xyz/info"
HEADERS = {"Content-Type": "application/json"}

def call(body: dict) -> dict:
    resp = requests.post(BASE_URL, json=body, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()


def dtms(dt:datetime) -> int:
    """
    Convert a (timezone-aware) datetime to epoch milliseconds, useful to access historical data
    """
    dt_utc = dt.astimezone(timezone.utc)
    return int(dt_utc.timestamp() * 1000)
