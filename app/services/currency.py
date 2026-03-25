import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API")

def get_rate(from_currency: str, to_currency: str) -> float:
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    
    response = requests.get(url)
    data = response.json()

    if data["result"] != "success":
        raise Exception("API error")

    return data["conversion_rates"][to_currency]