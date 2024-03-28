#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import *
from flight_search import *
from datetime import datetime, timedelta
from notification_manager import *

data_manager = DataManager()
flight_search = FlightSearch()
sms = NotificationManager()

# sheety_data = data_manager.get_data_sheet()["arkusz1"]  |
# Ograniczona liczba zapytan do Sheety, tymczasowa lista \./

sheety_data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
               {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
               {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
               {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
               {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
               {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
               {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
               {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
               {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]

#
# for x in sheety_data:
#     city_code = flight_search.get_IATA_code(x['city'])    Zadziałało, aktualnie niepotrzbne generowanie zapytań
#     data_manager.update_IATA_code(city_code, x["id"])

today = datetime.today().strftime("%d/%m/%Y")
six_m_later = datetime.today() + timedelta(6*30)
formated_sml = six_m_later.strftime("%d/%m/%Y")

for x in sheety_data:
    chepest = flight_search.check_cheapest_flight(x["iataCode"], 1000, today, formated_sml)
    if chepest:
        # sms.send_mesage(chepest[0], x["city"], x["iataCode"], chepest[1])
        print(chepest[0], x["city"], x["iataCode"], chepest[1])

    else:
        print("Brak latów w tej cenie")

