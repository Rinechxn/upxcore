import requests

# The URL of the API endpoint
url = 'http://api.uppriez.net:4000/songs/wav'

# Making a GET request to the API
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the response JSON into a dictionary
    data = response.json()
    print(data)
else:
    print(f"Failed to fetch data: {response.status_code}")
