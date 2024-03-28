import requests
import os
AFFIID_KIWI = os.environ['AFFIID_KIWI']
TOKEN_KIWI = os.environ['TOKEN_KIWI']
APPI_END_POINT_KIWI = os.environ['APPI_END_POINT_KIWI']

APPI_HEADER_KIWI = {
    "accept": "application/json",
    "apikey": TOKEN_KIWI
}
# 01/05/2024
# 03/11/2024
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_IATA_code(self, city):
        endpoit = APPI_END_POINT_KIWI + "locations/query"
        params = {
                "term": city,
                "locale": "en-US",
                "location_types": "airport",
                "limit": 1
        }
        response = requests.get(url=endpoit, params=params, headers=APPI_HEADER_KIWI).json()
        return response["locations"][0]["city"]["code"]



    def check_cheapest_flight(self, destination, price, date_from, date_to):
        endpoint = APPI_END_POINT_KIWI + "v2/search"
        param = {
            "fly_from": "PL",
            "fly_to": destination,
            "date_from": date_from,
            "date_to": date_to,
            "max_fly_duration": 20,
            "one_for_city": 0,
            "adults": 1,
            "children": 0,
            "selected_cabins": "M",
            "adult_hold_bag": 1,
            "adult_hand_bag": 1,
            "only_working_days": "false",
            "only_weekends": "false",
            "curr": "EUR",
            "price_to": price,
            "max_stopovers": 0,
            "max_sector_stopovers": 0,
            "vehicle_type": "aircraft",
            "limit": 1
        }
        response = requests.get(url=endpoint, params=param, headers=APPI_HEADER_KIWI).json()
        price_date = []
        # for x in response['data']:
        #     price.append(x["price"])
        if len(response["data"]) > 0:
            price_date.append(response["data"][0]["price"])
            date = response["data"][0]["local_departure"]
            price_date.append(date[:10])
            return price_date
        else:
            return False
        # return price