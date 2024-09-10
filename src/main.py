import json
from data_getter import fetch_pepsico_data

def main():
    data = fetch_pepsico_data()
    if data:
        print("Data fetched successfully.")
        # Pretty-print the first few lines of the JSON data
        # We will limit the printing to the first level of keys
        print(json.dumps(data, indent=4)[:1000])  # Print first 1000 characters of the JSON payload
    else:
        print("Failed to fetch or verify data.")

if __name__ == "__main__":
    main()
