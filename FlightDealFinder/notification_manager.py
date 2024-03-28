import twilio.rest
import os
MY_NUMBER = os.environ['MY_NUMBER']
FROM_NR = os.environ['FROM_NR']
SID_TWILIO = os.environ['SID_TWILIO']
TOKEN_TWILIO = os.environ['TOKEN_TWILIO']



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_mesage(self, price, dest_city, dest_IATA, data):
        client = twilio.rest.Client(SID_TWILIO, TOKEN_TWILIO)
        message = client.messages \
            .create(
            body=f"Only {price} ojro to fly from Warsaw - WAW to {dest_city}-{dest_IATA}, from {data}",
            from_=FROM_NR,
            to=MY_NUMBER
        )
