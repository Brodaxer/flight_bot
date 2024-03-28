import requests
import os
ENDPOINT_SHEETY = os.environ['ENDPOINT_SHEETY']
TOKEN_SHEETY = os.environ['TOKEN_SHEETY']
HEADERS_SHEETY = {
            "Authorization": f"Bearer {TOKEN_SHEETY}"
        }
class DataManager:

    def get_data_sheet(self):
        response = requests.get(url=ENDPOINT_SHEETY, headers=HEADERS_SHEETY)
        return response.json()

    def update_IATA_code(self, IATA_code, row):
        updtae_endpoit = ENDPOINT_SHEETY + f"/{row}"
        param = {
            "arkusz1": {
                "iataCode": IATA_code
            }
        }
        requests.put(url=updtae_endpoit, headers=HEADERS_SHEETY, json=param)
