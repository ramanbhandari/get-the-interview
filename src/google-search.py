import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
ENGINE_ID = os.getenv('ENGINE_ID')
SEARCH_URL_1 = os.getenv('SEARCH_URL_1')
SEARCH_QUERY_1 = os.getenv('SEARCH_QUERY_1')

def custom_search(query, num_results=10, start=1):
    url = os.getenv(SEARCH_URL_1)
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

results = custom_search(os.getenv(SEARCH_QUERY_1))

if results:
    for item in results.get('items', []):
        print(item['link']) 