from pprint import pprint
import requests
#This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/9a3caf9829c37c69b0db2e03cce3d2a4/flightDeals/prices"
        self.response = requests.get(url= self.sheety_endpoint)
        self.response.raise_for_status()
        self.data = self.response.json()["prices"]
