import datetime as dt
from pprint import pprint
import os
import requests
class FlightData:
    #This class is responsible for structuring the flight data.
    def search_flight(self, code):
        header = {
            "apikey": os.environ.get("APIKEY")
        }
        endpoint = "https://tequila-api.kiwi.com/v2/search"
        time = dt.datetime.now() + dt.timedelta(weeks= 26.0887285)
        future_time = time.strftime("%d/%m/%Y")
        today = dt.datetime.now()
        today_day = today.strftime("%d/%m/%Y")
        local_iata = "TLV"
        parameters = {
            "fly_from": local_iata,
            "fly_to": code,
            "dateFrom": today_day,
            "dateTo": future_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round"
        }
        response = requests.get(url= endpoint, params= parameters, headers= header)
        data = response.json()
        return data["data"][0]



