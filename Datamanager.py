import requests, os
from FlightData import Flight

class Data:

    def __init__(self):
        self.api = os.environ.get('SHEETY_API')
        self.headers = {
            'Authorization': os.environ.get('SHEETY_HEADER')
        }
        self.get_post_url = f"https://api.sheety.co/{self.api}/flightDetails/flightDetails"
        self.data = requests.get(url = self.get_post_url, headers=self.headers).json()
        self.city_only = []
    
    def get_city(self):
        for index in range(0, len(self.data['flightDetails'])):
            city  = self.data['flightDetails'][index]['iataCode']
            self.city_only.append(city)

    def provide_tuple(self):
        tuple = []
        for index in range(0, len(self.data['flightDetails'])):
            city  = self.data['flightDetails'][index]['iataCode']
            budget = self.data['flightDetails'][index]['budget']
            tupled = (city, budget)
            tuple.append(tupled)
        return(tuple)
    
    def check_blank(self):
        for index in range(0, len(self.data['flightDetails'])):
            if self.data['flightDetails'][index]['iataCode'] == '':
                return True
            else: 
                pass

    def fill_blank_iata(self):
        for index in range(0, len(self.data['flightDetails'])):
            if self.data['flightDetails'][index]['iataCode'] == '':
                city = self.data['flightDetails'][index]['city']
                iataCode1 = Flight().search_iata_code(city=city)
                add = {
                    'flightDetail' : {
                        'iataCode': f'{iataCode1}'
                    }
                }
                obj_id  = int(index) + 2
                requests.put(url=f"{self.get_post_url}/{obj_id}", json=add, headers=self.headers)
            else:
                pass