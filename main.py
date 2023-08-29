from Datamanager import Data
from SearchFlight import FlightSearch
from FlightData import Flight
from notify import Notify
from new_user import NewUser
from email_subscribers import Subscribers

data_obj = Data()
flightsearch_obj = FlightSearch()
flight_data = Flight()
noti = Notify()
new = NewUser()
sub = Subscribers()

#This checks if there are any blank spaces within IATA Codes column and fill them according to the city.
def fill_iata():
    if data_obj.check_blank():
        data_obj.fill_blank_iata() 

#This function checks if the subscribed list is not empty.If the list of email is empty, 
# it asks a user to enter name and email address to send email. It requires atleast one email address.
def check_subscribers():
    if sub.check_subs():
        new.get_user()
    else: 
        pass

#This performs rest of the activity where it finds flight prices
fill_iata()
check_subscribers()
noti.compare_tuples()
