import json
import os

# Define the test file path
file_path = os.path.join('/Users', 'jundachen', 'code', 'stonks', 'Pepsi Test Data CIK0000077476.json')

# Load the test JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract the relevant facts
facts = data['facts']['us-gaap']

# Helper function to extract values from a specific field for all periods
def get_values(fact_name):
    fact = facts.get(fact_name, {})
    if 'units' in fact:
        if 'USD' in fact['units']:
            return fact['units']['USD']
    return []

# Get the values for each metric
net_cash_values = get_values('NetCashProvidedByUsedInOperatingActivities')
interest_expense_values = get_values('InterestExpense')
assets_values = get_values('Assets')
cash_values = get_values('CashAndCashEquivalentsAtCarryingValue')
liabilities_values = get_values('Liabilities')
short_term_borrowings_values = get_values('ShortTermBorrowings')

# Print out the values for each fact by quarter
print("Extracted Values for Each Quarter:")

for i in range(len(net_cash_values)):
    # Get the quarter end date for context
    end_date = net_cash_values[i]['end'] if i < len(net_cash_values) else "Unknown"

    print(f"\nQuarter Ending: {end_date}")

    # Extract and print Net Cash Provided By Operating Activities
    net_cash_provided = net_cash_values[i]['val'] if i < len(net_cash_values) else "Missing"
    print(f"Net Cash Provided By Operating Activities: {net_cash_provided}")

    # Extract and print Interest Expense
    interest_expense = interest_expense_values[i]['val'] if i < len(interest_expense_values) else "Missing"
    print(f"Interest Expense: {interest_expense}")

    # Extract and print Assets
    if i < len(assets_values):
        assets = assets_values[i]['val']
        print(f"Assets: {assets}")
    else:
        print("Assets: Missing - No data for this period")

    # Extract and print Cash and Equivalents
    if i < len(cash_values):
        cash_and_equivalents = cash_values[i]['val']
        print(f"Cash and Equivalents: {cash_and_equivalents}")
    else:
        print("Cash and Equivalents: Missing - No data for this period")

    # Extract and print Liabilities
    if i < len(liabilities_values):
        liabilities = liabilities_values[i]['val']
        print(f"Liabilities: {liabilities}")
    else:
        print("Liabilities: Missing - No data for this period")

    # Extract and print Short-Term Borrowings
    if i < len(short_term_borrowings_values):
        short_term_borrowings = short_term_borrowings_values[i]['val']
        print(f"Short-Term Borrowings: {short_term_borrowings}")
    else:
        print("Short-Term Borrowings: Missing - No data for this period")