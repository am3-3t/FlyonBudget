import requests, os
from Datamanager import Data

class FlightSearch():

    def __init__(self) -> None:
        self.header = {
               'apikey': os.environ.get('TEQUILA_API')
        }
        self.end_point = 'https://api.tequila.kiwi.com/v2/search'
        self.tupled2 = []

    def get_min_price(self, city):
        parameters = {
            'fly_from': 'LON',
            'fly_to': f'{city}',
            'date_from': '29/08/2023',
            'date_to': '05/09/2023',
            'max_stopovers': 0
        }   
        response = requests.get(url=self.end_point, params= parameters, headers=self.header)
        data = response.json()
        list = []
        for items in range(len(data['data'])):
            list.append(data['data'][items]['price'])

        try:
            minimum_price = (min(list))
            return minimum_price
        #Incase there are no flights and list is empty. The following will handle exception
        except ValueError:
            pass
        except UnboundLocalError: 
            pass

        


    def tuple_min_price(self):
        obj = Data()
        obj.get_city()
        list1 = obj.city_only
        tupled_list = []
        for cities in list1:
            least_price = self.get_min_price(city=cities)
            tupled2 = (cities, least_price)
            tupled_list.append(tupled2)
        
        return tupled_list 
    
        
            
        

