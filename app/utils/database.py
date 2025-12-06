from flask import jsonify
import json
import os

def read_locations_data(file_path='app/data/locations_data.json'):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        return json.load(file)

def write_locations_data(data, file_path='app/data/locations_data.json'):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)