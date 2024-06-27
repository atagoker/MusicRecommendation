import os
import requests

current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, 'datasets', 'raw')

os.makedirs(data_dir, exist_ok=True)

SPOTIFY_API_URL = "https://api.spotify.com/v1"

from dotenv import load_dotenv
load_dotenv()

SPOTIFY_API_TOKEN = os.getenv('SPOTIFY_API_TOKEN')

def get_headers():
    """Returns the headers required for making requests to the Spotify API."""
    return {
        "Authorization": f"Bearer {SPOTIFY_API_TOKEN}"
    }

def fetch_new_releases():
    """Fetches new releases from Spotify."""
    url = f"{SPOTIFY_API_URL}/browse/new-releases"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch new releases: {response.status_code}")

def save_data(data, filename):
    """Saves data to a file."""
    file_path = os.path.join(data_dir, filename)
    with open(file_path, 'w') as file:
        file.write(data)

def main():
    """Main function to collect and save data."""
    try:
        new_releases = fetch_new_releases()
        save_data(str(new_releases), 'new_releases.json')
        print("Data collection successful")
    except Exception as e:
        print(f"Error during data collection: {e}")

if __name__ == "__main__":
    main()

