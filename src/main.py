import json
import os

# Define the test file path
file_path = os.path.join(
    "/Users", "jundachen", "code", "stonks", "vital_farms_CIK0001579733.json"
)

# Load the test JSON file
with open(file_path, "r") as file:
    data = json.load(file)

# Extract the list of asset values
asset_entries = data["facts"]["us-gaap"]["Assets"]["units"]["USD"]

# Print condensed header for the table
print(f"{'End':<11}{'Value (USD)':>15}{'Fiscal Year':>5}{'Fiscal Period':>5}{'Form':>6}{'Filed':>12}")
print("-" * 55)

# Parse through each quarter and extract relevant information
for entry in asset_entries:
    end_date = entry.get("end")
    value = entry.get("val")
    fiscal_year = entry.get("fy")
    fiscal_period = entry.get("fp")
    form_type = entry.get("form")
    filing_date = entry.get("filed")

    # Print the condensed row
    print(f"{end_date:<11}{value:>15}{fiscal_year:>5}{fiscal_period:>5}{form_type:>6}{filing_date:>12}")