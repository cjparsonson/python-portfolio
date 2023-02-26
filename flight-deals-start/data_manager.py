# Imports
import os
import requests

from dotenv import load_dotenv

load_dotenv()

# Globals
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')
SHEETY_GET = os.getenv('SHEETY_GET')
SHEETY_PUT = os.getenv('SHEETY_PUT')


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, bearer_token, get_endpoint, put_endpoint):
        self.bearer_token = bearer_token
        self.get_endpoint = get_endpoint
        self.put_endpoint = put_endpoint
        self.auth_header = {"Authorization": f"Bearer {self.bearer_token}"}

    def get_location_rows(self) -> dict:
        response = requests.get(headers=self.auth_header, url=self.get_endpoint)
        response.raise_for_status()
        rows_data = response.json()
        return rows_data['prices']

    def update_iata_records(self, data_sheet: dict):
        for location in data_sheet:
            object_ID = location['id']
            object_URL = f"{SHEETY_PUT}{object_ID}"
            object_params = {
                "price": {
                    "iataCode": location['iataCode']
                }
            }
            response = requests.put(headers=self.auth_header, url=object_URL, json=object_params)
            response.raise_for_status()






