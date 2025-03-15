import os
from dotenv import load_dotenv
import smtplib
from flight_data import FlightData

load_dotenv()

class NotificationManager:
    '''
    This class is responsible for sending notifications with the deal flight details.
    '''
    def __init__(self):
    	self._mail_id = os.getenv('GMAIL_ID')
    	self._mail_pass = os.getenv('GMAIL_PASS')

    def send_text(self, my_preference, FlightData: FlightData):
    	flight = FlightData
    	if flight.price != "N/A" and float(my_preference['lowestPrice']) > float(flight.price) :
	    	s = smtplib.SMTP('smtp.gmail.com', 587)
	    	s.starttls()
	    	s.login(self._mail_id, self._mail_pass)
	    	msg = f"A flight from {flight.origin_airport} to {flight.destination_airport} is available on {flight.out_date} till {flight.return_date} at a price of £{flight.price}!".encode('utf8')
	    	s.sendmail(self._mail_id, self._mail_id, msg)
	    	s.quit()
