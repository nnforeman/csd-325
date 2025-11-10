# CSD-325 Module-9
# Name: Natasha Foreman

import requests
import json

# 1 — Test connection to the API
def test_connection(url):
    print("=== CONNECTION TEST ===")
    print("Testing:", url)
    try:
        response = requests.get(url, timeout=10)
        print("Status Code:", response.status_code)
    except Exception as e:
        print("Connection Error:", e)
    print("-----------------------\n")

# 2 — Get raw response (no formatting)
def get_raw_response(url):
    print("=== RAW RESPONSE (NO FORMATTING) ===")
    response = requests.get(url, timeout=10)
    print(response.text)   # raw JSON text
    print("-----------------------\n")
    return response


# 3 — Get formatted response (like tutorial)
def format_cat_fact(response):
    print("=== FORMATTED OUTPUT ===")
    try:
        data = response.json()
        fact = data.get("fact")
        length = data.get("length")
        print(f"Cat Fact ({length} characters):")
        print(f"- {fact}")
    except:
        print("Error formatting JSON.")
    print("-----------------------\n")


# MAIN PROGRAM
if __name__ == "__main__":

    url = "https://catfact.ninja/fact"

    # Step 1: Test connection
    test_connection(url)

    # Step 2: Raw response
    response = get_raw_response(url)

    # Step 3: Formatted response
    format_cat_fact(response)
