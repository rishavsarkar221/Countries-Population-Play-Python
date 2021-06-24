stocks = {
    "info": [600, 630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160]
}

userInput = input('''Enter Any one of the 2 commands
print - Prints all the stocks and prices
add - add a new stock and a new price
''')

print("\n")


def print_stocks(stock):
    for stock_name, stock_price in stock.items():
        average = round(sum(stock_price) / len(stock_price), 2)
        print(f"{stock_name} ==> {stock_price} ==> avg: {average}")


def add(stock):
    stock_name_input = input("Enter Stock name: ")

    try:
        stock_price_input = round(float(input("Enter Stock Price: ")))

        if stock_name_input in stock:
            stock[stock_name_input].append(stock_price_input)
            print("\n")
            print(f"Stock Name {stock_name_input} and Price {stock_price_input} Added Successfully!")
            return print_stocks(stock)
        else:
            stock[stock_name_input] = [stock_price_input]
            print("\n")
            print(f"Stock Name {stock_name_input} and Price {stock_price_input} Added Successfully!")
            return print_stocks(stock)

    except ValueError:
        print("Enter Numbers Only for Price")


if userInput.lower() == "print":
    print_stocks(stocks)
elif userInput.lower() == "add":
    add(stocks)
