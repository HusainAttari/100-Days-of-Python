import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_API_ENDPOINT = f"https://api.sheety.co/{os.getenv('SHEETY_API_ENDPOINT')}"

class DataManager:
    '''
    This class is responsible for talking to the Google Sheet.
    '''
    def __init__(self):
    	self._auth_header = {
    		'Authorization': f"Bearer {os.getenv('SHEETY_AUTH_TOKEN')}"
    	}
    	self.sheet_data = {}

    def get_sheet(self):
    	r = requests.get(SHEETY_API_ENDPOINT, headers=self._auth_header)
    	r.raise_for_status()
    	self.sheet_data = r.json()['prices']

    def update_iata(self, row_id, iata_code):
    	data = {
    		'price': {
    			'iataCode': iata_code
    		}
    	}
    	r = requests.put(url=f"{SHEETY_API_ENDPOINT}/{row_id}", json=data, headers=self._auth_header)
    	r.raise_for_status()
    	print(r.text)    	