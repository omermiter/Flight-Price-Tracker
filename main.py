#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager as dm
from flight_search import FlightSearch as fs
from flight_data import FlightData as fd
from pprint import pprint
from notification_manager import NotificationManager as nf
sheet_data = dm().data
for i in sheet_data:
    if i["iataCode"] == '':
        fs().find_iata(city= i["city"], id = i["id"])
        sheet_data = dm().data
    else:
        flights = fd().search_flight(code= i["iataCode"])
        price = int(flights["price"])
        if price < i["lowestPrice"]:
            nf().send_sms(price= price, dp_city= flights["cityFrom"], dp_iata= flights["flyFrom"], arr_city= flights["cityTo"], arr_iata= flights["flyTo"], outbound= flights["local_departure"], inbound=flights["route"][len(flights["route"]) - 1]["local_departure"])

print(sheet_data)


