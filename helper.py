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
    
def get_start_date():
    print("Please enter the start date :")
    year = int(input("Year (YYYY): "))
    month = int(input("Month (1-12): "))
    day = int(input("Day (1-31): "))
    hour = int(input("Hour (0-23): "))
    minute = int(input("Minute (0-59): "))
    delta = int(input("Timezone difference from UTC: "))
    
    start_date = datetime(
        year,          
        month,       
        day,          
        hour,      
        minute,         
        second=0,     
        microsecond=0,  
        tzinfo=timezone(timedelta(hours=delta))   
    )
    return start_date
