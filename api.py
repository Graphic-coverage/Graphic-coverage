import requests
import base64
import json

teams_names = {
    "9662": "apollo",
    "111992": "black tigers",
    # ... (rest of the teams_names dictionary)
}

# Shay's username and Authorization key
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

    # Dictionary to store team numbers and their corresponding data
    team_data = {}

    # Iterate through matches
    for match in data.get('matches', []):
        # Iterate through teams in each match

        for team in match.get('teams', []):
            team_number = team.get('teamNumber')
            station = team.get('station')
            if team_number is not None:
                # Create an empty dictionary for the team if it doesn't exist
                team_dict = team_data.setdefault(team_number, {})

                # Add data to the team's dictionary
                team_dict["team name"] = teams_names.get(str(team_number), "Unknown")
                team_dict["station"] = station

    # Print the structure for each team number
    for team_number, data in team_data.items():
        print(f"Team Number: {team_number}")
        print(json.dumps(data, indent=4))
        print("\n")

else:
    print(f"Request failed with status code {response.status_code}")
