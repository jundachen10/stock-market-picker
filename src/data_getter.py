
#data.sec.gov/api/xbrl/companyfacts/
#This API returns all the company concepts data for a company into a single API call:
#https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json

import requests
from config import BASE_URL, CIK, HEADERS

def fetch_pepsico_data():
    """Fetch financial data for PepsiCo from the SEC EDGAR API and verify the JSON payload."""
    url = f"{BASE_URL}CIK{CIK}.json"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raises an HTTPError if the status is 4xx or 5xx
        data = response.json()  # Ensure the response is in JSON format
        print("JSON data successfully retrieved and verified.")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except ValueError:
        print("Error: Response is not valid JSON.")
        return None
