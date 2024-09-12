import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
ENGINE_ID = os.getenv('ENGINE_ID')

def custom_search(query, num_results=10, start=1):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'key': API_KEY,
        'cx': ENGINE_ID,
        'num': num_results,
        'start': start,
        'fileType': 'pdf',
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

query = 'resume software engineer google'
results = custom_search(query)

if results:
    for item in results.get('items', []):
        print(item['link']) 