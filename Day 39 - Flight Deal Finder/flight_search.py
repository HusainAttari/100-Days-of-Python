import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

IATA_ENDPOINT = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
AUTH_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'
FLIGHT_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightSearch:
    '''
    This class is responsible for talking to the Flight Search API.
    '''
    def __init__(self):
    	self._api_key = os.getenv("AMADEUS_API_KEY")
    	self._api_secret = os.getenv("AMADEUS_API_SECRET")
    	self._token = self._get_new_token()

    def _get_new_token(self):
    	params = {
    		'grant_type': 'client_credentials',
    		'client_id': self._api_key,
    		'client_secret': self._api_secret,
    	}

    	header = {
    		'Content-Type': 'application/x-www-form-urlencoded',
    	}

    	r = requests.post(url=AUTH_ENDPOINT, data=params, headers=header)
    	r.raise_for_status()
    	token = r.json()['access_token']
    	return token

    def get_iata(self, city:str) -> str :
    	parameters = {
    		'keyword': city,
    		'max': 1,
    	}
    	auth_header = {
    		'Authorization': f"Bearer {self._token}",
    	}

    	r = requests.get(url=IATA_ENDPOINT, params=parameters, headers=auth_header)
    	r.raise_for_status()
    	try:
    		iata_code = r.json()['data'][0]['iataCode']
    	except KeyError:
    		print(f"KeyError : No airport code found for {city}")
    		return "N/A"
    	except IndexError:
    		print(f"IndexError : No airport code found for {city}")
    		return "Not Found"
    	return iata_code

    def find_flights(self, origin_city, destination_city, from_time, to_time, max_price):
    	header = {'Authorization': f"Bearer {self._token}"}
    	query = {
    		'originLocationCode': origin_city,
    		'destinationLocationCode': destination_city,
    		'departureDate': from_time.strftime("%Y-%m-%d"),
    		'returnDate': to_time.strftime("%Y-%m-%d"),
    		#'maxPrice': int(max_price),
    		'adults': 1,
    		'nonStop': 'true',
    		'currencyCode': 'GBP',
    		'max': 10,
    	}

    	r = requests.get(url=FLIGHT_SEARCH_ENDPOINT, params=query, headers=header)
    	r.raise_for_status()
    	return r.json()