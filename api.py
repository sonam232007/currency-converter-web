import requests
import os

API_KEY = os.getenv("API_KEY")

def convert_currency(amount, from_currency, to_currency):

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        if data["result"] == "success":

            rate = data["conversion_rates"].get(to_currency)

            if rate:

                converted = amount * rate

                return converted, rate

    return None, None