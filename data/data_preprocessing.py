import os
import json

current_dir = os.path.dirname(__file__)
raw_data_dir = os.path.join(current_dir, 'datasets', 'raw')
processed_data_dir = os.path.join(current_dir, 'datasets', 'processed')

os.makedirs(processed_data_dir, exist_ok=True)

def process_data(input_filename, output_filename):
    """Processes raw data and saves it in a cleaned format."""
    input_path = os.path.join(raw_data_dir, input_filename)
    output_path = os.path.join(processed_data_dir, output_filename)
    
    with open(input_path, 'r') as infile:
        data = json.load(infile)
    
    processed_data = [track['name'] for track in data['albums']['items']]
    
    with open(output_path, 'w') as outfile:
        json.dump(processed_data, outfile, indent=4)

def main():
    """Main function to preprocess and save data."""
    try:
        process_data('new_releases.json', 'processed_new_releases.json')
        print("Data preprocessing successful")
    except Exception as e:
        print(f"Error during data preprocessing: {e}")

if __name__ == "__main__":
    main()

