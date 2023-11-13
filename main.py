import requests
import base64
import json

# shay's username and Authorization key
username = "shayapi"
authorization_key = "0B7728C5-E529-478F-B53D-FA3F95A1CCF4"

# Combine and encode the credentials
credentials = f'{username}:{authorization_key}'.encode('utf-8')
base64_credentials = base64.b64encode(credentials).decode('utf-8')

# Set up the headers with the Authorization header using the base64-encoded credentials
headers = {
    'Authorization': f'Basic {base64_credentials}'
}


# URL of the API endpoint you want to access
season = 2022
regionCode = "ILCMPSOLR"
api_url = f"http://ftc-api.firstinspires.org/v2.0/{season}/matches/{regionCode}"

# Make a GET request to the API with the correct headers
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Pretty print the JSON data with indentation for readability
    print(json.dumps(data, indent=4))
else:
    print(f"Request failed with status code {response.status_code}")
