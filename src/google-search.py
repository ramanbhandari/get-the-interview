import requests
import os
import sqlite3
import time
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
ENGINE_ID = os.getenv('ENGINE_ID')
SEARCH_URL_1 = os.getenv('SEARCH_URL_1')
SEARCH_QUERY_1 = os.getenv('SEARCH_QUERY_1')
SEARCH_QUERY_2 = os.getenv('SEARCH_QUERY_2')

conn = sqlite3.connect('urls.db')
cursor = conn.cursor()

def fetch_urls(num_results=10, start=1):
    params = {
        'q': SEARCH_QUERY_2,
        'key': API_KEY,
        'cx': ENGINE_ID,
        'num': num_results,
        'start': start,
    }

    try:
        response = requests.get(SEARCH_URL_1, params=params)
        response.raise_for_status()
        data = response.json()

        if 'items' in data:
            return data['items']
        elif 'error' in data:
            print(f"API Error: {data['error']['message']}")
        else:
            print("Unexpected response format.")
        
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

    return []

def store_urls(urls):
    for item in urls:
        url = item.get('link')
        title = item.get('title', 'No Title')

        try:
            cursor.execute("INSERT OR IGNORE INTO urls (url, title) VALUES (?, ?)", (url, title))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting URL in DB: {e}")

def main():
    start_index = 71
    results_per_request = 10

    for _ in range(5):
        urls = fetch_urls(results_per_request, start_index)
        if not urls:
            break
        store_urls(urls)
        start_index += results_per_request

        time.sleep(2)
    print("Finished fetching and storing URLS")

if __name__ == "__main__":
    main()

conn.close()