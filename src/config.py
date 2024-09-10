# config.py
BASE_URL = "https://data.sec.gov/api/xbrl/companyfacts/"
CIK = "0000077476"  # CIK for PepsiCo, Inc.
HEADERS = { #not sure about this part may remove later
    "User-Agent": "j3asy",
    "Accept-Encoding": "gzip, deflate",
    "Host": "data.sec.gov",
}
