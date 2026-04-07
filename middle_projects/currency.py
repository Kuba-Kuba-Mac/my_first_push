def show_menu():
    print("Currencies for trade ")
    print("1. Dollar to Som ")
    print("2. Dollar to Tenge ")
    print("3. Dollar to Ruble ")



while True:
    show_menu()

    choice  = int(input("Enter number fo trade (1-3) or 0 is stop: "))
    num1 = int(input("Enter a quantity of currency to trade : "))

    if choice == 1:
        print(f"{num1* 87.7} som" )
    elif choice == 2:
        print(f"{464.78*num1} tenge ")
    elif choice == 3:
        print(f"{num1*78.67} ruble ")
    elif choice == 0:
        break
    else : print("Please enter a valid number ")



import requests

def convert_currency():
    base = input("From currency (e.g. USD): ").upper()
    target = input("To currency (e.g. EUR): ").upper()
    amount = float(input("Enter amount: "))

    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data")
        return

    data = response.json()

    rates = data["rates"]

    if target not in rates:
        print("Invalid target currency")
        return

    result = amount * rates[target]

    print(f"{amount} {base} = {result:.2f} {target}")

convert_currency()
