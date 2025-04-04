class FlightData:
	'''
	This class is responsible for structuring the flight data.
	'''
	def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
		self.price = price
		self.origin_airport = origin_airport
		self.destination_airport = destination_airport
		self.out_date = out_date
		self.return_date = return_date

def find_cheapest_flight(data: dict):
	# Check for empty data
	if data is None or not data['data'] :
		print("No flight data available :(")
		return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

	# Data from the first flight in the json
	first_flight = data['data'][0]
	lowest_price = float(first_flight['price']['grandTotal'])
	origin = first_flight['itineraries'][0]['segments'][0]['departure']['iataCode']
	destination = first_flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
	departure_date = first_flight['itineraries'][0]['segments'][0]['departure']['at'].split("T")[0]
	arrival_date = first_flight['itineraries'][0]['segments'][0]['arrival']['at'].split("T")[0]

	cheapest_flight = FlightData(lowest_price, origin, destination, departure_date, arrival_date)

	for flight in data['data']:
		price = float(flight['price']['grandTotal'])
		if price < lowest_price :
			lowest_price = price
			origin = first_flight['itineraries'][0]['segments'][0]['departure']['iataCode']
			destination = first_flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
			departure_date = first_flight['itineraries'][0]['segments'][0]['departure']['at'].split("T")[0]
			arrival_date = first_flight['itineraries'][0]['segments'][0]['arrival']['at'].split("T")[0]

			cheapest_flight = FlightData(lowest_price, origin, destination, departure_date, arrival_date)

	return cheapest_flight