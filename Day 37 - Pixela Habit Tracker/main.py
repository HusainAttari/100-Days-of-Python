import requests
from datetime import datetime

# Refer to Pixela API documentation for valid values
USER = '<Enter your username>'
TOKEN = '<Enter your token>'
GRAPH_ID = '<Enter graph id>'

user_endpoint = 'https://pixe.la/v1/users'

user_parameters = {
	'token': TOKEN,
	'username': USER,
	'agreeTermsOfService': 'yes',
	'notMinor': 'yes',
}

# Only run once
response = requests.post(user_endpoint, json=user_parameters)
print(response.text)

graph_endpoint = f"{user_endpoint}/{USER}/graphs"

graph_parameters = {
	'id': GRAPH_ID,
	'name': 'Pages I Read Today!',
	'unit': 'Pages',
	'type': 'int',
	'color': 'momiji',
	'timezone': 'Asia/Kolkata',
}

header = {
	'X-USER-TOKEN': TOKEN,
}

# Only run once
r = requests.post(graph_endpoint, json=graph_parameters, headers=header)
print(r.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now().strftime('%Y%m%d')

pixel_data = {
	'date': today,
	'quantity': input("How many pages did you read today? : "),
}

r = requests.post(pixel_endpoint, json=pixel_data, headers=header)
print(r.text)

# pixel_update_data = {
# 	'quantity': '50',
# }

# r = requests.put(f'{pixel_endpoint}/{today}', json=pixel_update_data, headers=header)
# print(r.text)
