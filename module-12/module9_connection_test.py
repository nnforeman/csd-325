# CSD-325 Module-9 — API Connection Test
# Name: Natasha Foreman

import requests

def test(url):
    try:
        r = requests.get(url, timeout=10)
        print(f"URL: {url}") 
        print(f"Status code: {r.status_code}")
    except Exception as e:
        print(f"URL: {url}")
        print(f"Error: {e}")
    print("-" * 40)

if __name__ == "__main__":
    # Tutorial example: test a simple site connection
    test("http://www.google.com")

    # Reading List API (astronauts) — correct URL
    test("http://api.open-notify.org/astros.json")
