import requests
import json
import time

# Server URL
url = 'http://localhost:10001/api/coordinates'

# Data to be sent
data = {'index': 0}

while True:
    # Send a POST request
    response = requests.post(url, json=data)

    # Parse the response JSON data
    coordinates = response.json()

    # Print the complete JSON data returned by the server
    #print('Received data:', coordinates)

    # Extract latitude, longitude, and altitude from the coordinate data
    try:
        latitude = coordinates['latitude']
        longitude = coordinates['longitude']
        altitude = coordinates['altitude']

        # Print the received coordinate values
        print('Received coordinates: Latitude:', latitude, 'Longitude:', longitude, 'Altitude:', altitude)
    except KeyError:
        print('Could not extract coordinates from the received data.')

    # Wait for a while before sending the next request
    time.sleep(0.3)
