from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Read the path.json file
with open('path.json', 'r') as f:
    data = json.load(f)
path = data['path']  # Extract the 'path' value from data

# Initialize the index
index = 0

@app.route('/api/coordinates', methods=['POST'])
def post_coordinates():
    global index  # Use the global variable index

    # Extract the specified point from the path
    point = path[index]
    latitude = point['latitude']
    longitude = point['longitude']
    altitude = point['altitude']

    # Update the index, if it has reached the last point, reset it to 0
    index = (index + 1) % len(path)

    # Return the received coordinates
    return jsonify({'latitude': latitude, 'longitude': longitude, 'altitude': altitude}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10001)
