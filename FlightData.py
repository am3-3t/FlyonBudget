import requests, os

class Flight():

    def __init__(self):
        self.teq_api = os.environ.get('TEQUILA_API')
        self.headers = {
            'apikey': self.teq_api
        }
        self.teq_url = 'https://api.tequila.kiwi.com/locations/query'

    def search_iata_code(self, city):
        parameters = {
            "term": f'{city}'
        }
        response  = requests.get(url= self.teq_url, params=parameters, headers=self.headers)
        data = response.json()
        iata_code = data['locations'][0]['code']
        return iata_code
