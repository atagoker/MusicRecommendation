import os
import json

current_dir = os.path.dirname(__file__)
raw_data_dir = os.path.join(current_dir, '..', 'data', 'datasets', 'raw')

def load_json(filename):
    file_path = os.path.join(raw_data_dir, filename)
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, filename):
    file_path = os.path.join(raw_data_dir, filename)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
