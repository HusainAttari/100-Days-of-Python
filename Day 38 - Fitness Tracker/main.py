import os
import requests
from datetime import datetime

MY_WEIGHT = # YOUR WEIGHT IN KGS
MY_HEIGHT = # YOUR HEIGHT IN CMS
MY_AGE = # YOUR AGE

# All of the below data (App ID, API Key, Sheety Auth Token [if any], Sheety API Endpoint) are to be stored as environment variables since they contain sensitive data

APP_ID = YOUR NUTRITIONIX APP ID
API_KEY = YOUR NUTRITIONIX API KEY
SHEETY_AUTH_TOKEN = YOUR SHEETY APP TOKEN

sheety_endpoint = f'https://api.sheety.co/{YOUR_SHEETY_API_ENDPOINT}'

sheety_auth_header = {
	'Authorization': f"Bearer {SHEETY_AUTH_TOKEN}"
}

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutritionix_auth_header = {
	'x-app-id': APP_ID,
	'x-app-key': API_KEY,
}

nutritionix_params = {
	'query': input("What exercise did you do today? : "),
	'weight_kg': MY_WEIGHT,
	'height_cm': MY_HEIGHT,
	'age': MY_AGE
}

nutritionix_response = requests.post(nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_auth_header)
nutritionix_response.raise_for_status()
data = nutritionix_response.json()['exercises']

date = datetime.now()

for exercise in data :
	workout_data = {
		'workout': {
			'date': date.strftime('%d/%m/%Y'),
			'time': date.strftime('%I:%M:%S %p'),
			'exercise': exercise['name'].title(),
			'duration': exercise['duration_min'],
			'calories': exercise['nf_calories'],
		}
	}
	sheety_response = requests.post(sheety_endpoint, json=workout_data, headers=sheety_auth_header)
	sheety_response.raise_for_status()
	print(sheety_response.text)
