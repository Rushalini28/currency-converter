
import requests

def currency_converter():
    print("=" * 40)
    print("        CURRENCY CONVERTER")
    print("=" * 40)

    print("\nAvailable currencies:")
    print("INR - Indian Rupee")
    print("USD - US Dollar")
    print("EUR - Euro")
    print("GBP - British Pound")
    print("JPY - Japanese Yen")
    print("CAD - Canadian Dollar")
    print("AUD - Australian Dollar")

    try:
        amount = float(input("\nEnter amount to convert: "))

        if amount <= 0:
            print("Please enter an amount greater than zero.")
            return

        from_currency = input(
            "Convert from (example: INR): "
        ).strip().upper()

        to_currency = input(
            "Convert to (example: USD): "
        ).strip().upper()

        url = (
            f"https://open.er-api.com/v6/latest/"
            f"{from_currency}"
        )

        print("\nFetching exchange rate...")

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("result") != "success":
            print("Invalid source currency. Please try again.")
            return

        rates = data.get("rates", {})

        if to_currency not in rates:
            print("Invalid target currency. Please try again.")
            return

        rate = rates[to_currency]
        converted_amount = amount * rate

        print("\n" + "=" * 40)
        print("         CONVERSION RESULT")
        print("=" * 40)
        print(f"From currency : {from_currency}")
        print(f"To currency   : {to_currency}")
        print(f"Exchange rate : 1 {from_currency} = "
              f"{rate:.4f} {to_currency}")
        print(f"Original amount: {amount:.2f} {from_currency}")
        print(f"Converted amount: {converted_amount:.2f} "
              f"{to_currency}")
        print("=" * 40)

    except ValueError:
        print("Invalid amount! Please enter a number.")

    except requests.exceptions.RequestException:
        print("Unable to fetch exchange rates.")
        print("Check your internet connection and try again.")


currency_converter()
