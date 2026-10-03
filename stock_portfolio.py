# CodeAlpha Task 2: Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

total_investment = 0

try:
    number_of_stocks = int(
        input("\nHow many different stocks do you want to buy? ")
    )

    if number_of_stocks <= 0:
        print("Please enter a positive number.")
    else:
        for i in range(number_of_stocks):
            stock_name = input(
                f"\nEnter stock name #{i + 1}: "
            ).upper().strip()

            if stock_name not in stock_prices:
                print("Stock not available.")
                continue

            try:
                quantity = int(
                    input(f"Enter quantity of {stock_name}: ")
                )

                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue

                price = stock_prices[stock_name]
                investment = price * quantity
                total_investment += investment

                print(f"Price per share: ${price}")
                print(f"Investment in {stock_name}: ${investment}")

            except ValueError:
                print("Please enter a valid quantity.")

        print("\n================================")
        print("Total Investment: $", total_investment)
        print("================================")

except ValueError:
    print("Please enter a valid number.")
