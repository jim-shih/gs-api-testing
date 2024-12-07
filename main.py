import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv("../.env")

# Get credentials from .env file
API_KEY = os.getenv("API_KEY")
CSE_ID = os.getenv("CSE_ID")


def google_search(query):
    # Construct the URL with required parameters
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": API_KEY,
        "cx": CSE_ID,
        "q": query,
        "num": 10,  # Number of results (max 10 per page)
    }

    try:
        # Send GET request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise exception for bad status codes

        # Parse response
        search_results = response.json()
        return search_results.get("items", [])

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return []


def main():
    # Search query
    query = "best banks in Taiwan rankings financial stability"

    # Get search results
    results = google_search(query)

    # Print results
    print("\n=== Best Banks in Taiwan Search Results ===\n")

    for i, item in enumerate(results, 1):
        print(f"Result {i}:")
        print(f"Title: {item['title']}")
        print(f"Description: {item['snippet']}")
        print(f"URL: {item['link']}")
        print("-" * 80 + "\n")


if __name__ == "__main__":
    main()
