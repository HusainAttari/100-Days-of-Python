#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight

# Initialising various objects 
dataManager = DataManager()
flightSearch = FlightSearch()

ORIGIN_CITY_IATA = 'LON'

dataManager.get_sheet() # GETs the google sheet data

# For all empty IATA fields, a new IATA code is generated
for row in dataManager.sheet_data :
	if row['iataCode'] == '' :
		row['iataCode'] = flightSearch.get_iata(row['city']) # Updates the IATA code in the memory
		dataManager.update_iata(row['id'], row['iataCode']) # Updates the IATA codes in the google sheet
		time.sleep(2)

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=180)

for destination in dataManager.sheet_data :
	flights = flightSearch.find_flights(ORIGIN_CITY_IATA, destination['iataCode'], tomorrow, six_months_from_today, destination['lowestPrice'])
	cheapest_flight = find_cheapest_flight(flights)
	print(f"{destination['city']} : £{cheapest_flight.price}")

	time.sleep(2)