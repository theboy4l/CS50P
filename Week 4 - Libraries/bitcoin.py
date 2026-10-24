import sys
import requests

# Replace this non-working placeholder privately if you want to run the API request.
API_KEY = "YOUR_API_KEY_HERE"


def main():
    get_api()


def get_api():
    try:
        user_input = get_input()
        url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            response_data = response.json()
            innerdict = response_data.get("data")
            price_usd = float(innerdict.get("priceUsd"))
            final_price = user_input * price_usd
            print("$" + f"{final_price:,.4f}")
        else:
            sys.exit("Error!")
    except requests.RequestException:
        sys.exit("Could not reach API")


def get_input():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        userinput = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    return userinput


main()
