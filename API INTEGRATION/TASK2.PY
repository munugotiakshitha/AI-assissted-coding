
import requests

API_URL = "https://api.frankfurter.app/latest"
TARGET_CURRENCIES = ["USD", "EUR", "GBP"]


def convert_currency(amount):
    try:
        response = requests.get(
            API_URL,
            params={
                "amount": amount,
                "from": "INR",
                "to": ",".join(TARGET_CURRENCIES)
            },
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        rates = data.get("rates", {})

        if not all(currency in rates for currency in TARGET_CURRENCIES):
            print("Error: Exchange rates are missing from the response.")
            return

        print("\n--- Currency Conversion Results ---")
        print(f"{'Currency':<15}{'Converted Amount':>20}")
        print("-" * 35)

        for currency in TARGET_CURRENCIES:
            print(f"{currency:<15}{rates[currency]:>20.4f}")

        print(f"\nOriginal amount: INR {amount:.2f}")
        print("Note: Rates may not be real-time market prices.")

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: Check your internet connection.")
    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")
    except (requests.exceptions.RequestException, ValueError) as error:
        print(f"Error retrieving exchange rates: {error}")


if __name__ == "__main__":
    try:
        amount = float(input("Enter amount in INR: ").strip())

        if amount <= 0:
            print("Error: Amount must be greater than zero.")
        else:
            convert_currency(amount)

    except ValueError:
        print("Error: Please enter a valid numeric amount.")
