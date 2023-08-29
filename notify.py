from Datamanager import Data
from SearchFlight import FlightSearch
from twilio.rest import Client
from email_subscribers import Subscribers
import os


class Notify:
    def __init__(self) -> None:
        pass

    def send_notification(self, body1):
        account_sid = os.environ.get('TWILIO_ACC_SID')
        auth_token = os.environ.get('TWILIO_AUTH')
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_='+16189823410',
        body= f'{body1}',
        to='+9779861890463'
        )

    def compare_tuples(self): 
        tuple1_list = Data().provide_tuple()
        tuple2_list = FlightSearch().tuple_min_price()
        print(tuple1_list)
        print(tuple2_list)
        
        for (a, price1), (b, price2) in zip(tuple1_list, tuple2_list):
        
            #Incase there are no flights and list is empty. The following will handle exception. 
            # None type and Int will not be compared. Hence, type error must be handled.
            try:
                if price2 < price1:
                    try:
                        message = f'Price Drop Alert: LON ▶️  {a}. Fare to {a} is low by EUR {price1 - price2}, Fare: {price2}'
                        Subscribers().send_email(message=message)
                        print(message)
                        #Enable this 👇 to send message by setting up twilio account.
                        # self.send_notification(body1=message)
                    except TypeError:
                        print(f'There is no flight to {a}')
                else:
                    pass
            except TypeError:
                pass
        

    

         