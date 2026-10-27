# 💱 Currency Converter Using Python

## 📌 About the Project

The Currency Converter is a Python application that converts an amount from one currency to another using exchange rates fetched from an online API.

It allows users to enter an amount, select the source and target currencies, and view the converted amount based on the latest available exchange rate returned by the API.

## ✨ Features

- Converts amounts between different currencies.
- Fetches exchange rates online.
- Supports currencies such as INR, USD, EUR, GBP, JPY, CAD, and AUD.
- Displays the exchange rate and converted amount.
- Validates user input.
- Handles network errors and invalid currency codes.
- Simple and beginner-friendly interface using the terminal.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Library:** Requests
- **API:** ExchangeRate-API (open.er-api.com)

## 📂 Project Structure

```text
Currency Converter/
│
└── main.py
```

## ⚙️ Requirements

- Python 3.x
- Internet connection
- Requests library

## 🚀 Installation and Setup

### Step 1: Install Python

Download Python from https://www.python.org/downloads/ if it is not already installed.

### Step 2: Install the Requests Library

Open the terminal in VS Code and run:

```bash
python -m pip install requests
```

### Step 3: Run the Application

Navigate to the project folder and execute:

```bash
python main.py
```

### Step 4: Enter the Details

Enter the amount you want to convert, followed by the source currency code and target currency code.

## 💻 Example Usage

```text
CURRENCY CONVERTER

Available currencies:
INR - Indian Rupee
USD - US Dollar
EUR - Euro
GBP - British Pound
JPY - Japanese Yen
CAD - Canadian Dollar
AUD - Australian Dollar

Enter amount to convert: 100
Convert from (example: INR): USD
Convert to (example: INR): INR

Fetching exchange rate...
```

The program then displays the exchange rate and converted amount. The actual result depends on the rate returned by the API.

## 📚 Concepts Learned

- Python functions
- Variables and data types
- User input and output
- Exception handling using `try-except`
- Making HTTP requests
- Working with JSON data
- API integration
- Basic input validation

## ⚠️ Limitations

- An internet connection is required to fetch exchange rates.
- Exchange rates can change over time.
- The displayed conversion may not include bank charges or transaction fees.
- Actual exchange rates depend on the API response.

## 🔮 Future Improvements

- Create a graphical user interface using Tkinter.
- Add a dropdown list for currency selection.
- Add a currency swap button.
- Display conversion history.
- Support more currencies.
- Add historical exchange-rate charts.

## 👨‍💻 Author

Created as a beginner-friendly Python project to practise API integration and programming fundamentals.
