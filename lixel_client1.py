import requests
import json
import time

# Server URL
url = 'https://5gdive.bigdataiot.com.tw/FlyBehaviors/GetDroneDataForLixel'

# Data to be sent
data = {'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ._yCgxmq2L3w4pRw9BUOx8ItIVKLTgC9UmhnfncovZZ4'}

while True:
    # Send a POST request
    response = requests.post(url, json=data)

    # Parse the response JSON data
    coordinates = response.json()

    print('Received data:', coordinates)

    # Print the complete JSON data returned by the server
    print('Received data1:', coordinates)

    '''
    # Extract latitude, longitude, and altitude from the coordinate data
    try:
        latitude = coordinates['latitude']
        longitude = coordinates['longitude']
        altitude = coordinates['Alt']

        # Print the received coordinate values
        print('Received coordinates: Latitude:', latitude, 'Longitude:', longitude, 'Altitude:', altitude)
    except KeyError:
        print('Could not extract coordinates from the received data.')
    '''
    

    # Wait for a while before sending the next request
    time.sleep(0.3)
