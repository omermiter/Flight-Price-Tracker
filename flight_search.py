import requests
import datetime as dt
import os
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def make_ita(self, id, iata):
        urle = f"https://api.sheety.co/9a3caf9829c37c69b0db2e03cce3d2a4/flightDeals/prices/{id}"
        parameters = {
            "price": {
                "iataCode": iata
            }
        }
        response = requests.put(url= urle, json= parameters)
        response.raise_for_status()



    def find_iata(self, city, id):
        endpoint = "https://tequila-api.kiwi.com/locations/query"
        header = {
            "apikey": os.environ.get("APIKEY")
        }

        parameters = {
            "term": city,
            "location_types": "airport"
        }
        response = requests.get(url= endpoint, params= parameters, headers= header)
        data = response.json()["locations"]
        code = data[0]["city"]["code"]
        self.make_ita(id= id, iata= code)