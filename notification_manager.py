from twilio.rest import Client
import os
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.ACC_SID = os.environ.get("ACCSID")
        self.Token = os.environ.get("TOKEN")
    def send_sms(self,price, dp_city, dp_iata, arr_city, arr_iata, outbound, inbound):
        client = Client(self.ACC_SID, self.Token)
        sliced_text = slice(10)
        message = client.messages \
            .create(
            body=f"Low price alert! Only {price * 3.80}₪ to fly from {dp_city}-{dp_iata} to {arr_city}-{arr_iata}, from {outbound[sliced_text]} to {inbound[sliced_text]}",
            from_='+15756005603',
            to='+972544409502'
        )