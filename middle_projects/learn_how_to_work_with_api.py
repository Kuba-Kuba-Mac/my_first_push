from http.client import responses

import requests

#
username = input("Enter any username : ")
url = f"https://api.github.com/users/{username}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Имя: {data['name']}")
    print(f"Репозитории: {data['public_repos']}")
    print(f"Дата регистрации: {data['created_at']}")
#
#
#
#

url = f"https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    joke = data['setup']
    ans = data['punchline']
    print(f"{joke}   {ans}")
#
#
#
#
#
while True:
    base  = input("Chose one of them (USD || EUR) :").upper()
    amount = float(input("Write amount of currency :"))
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data")
        break

    data = response.json()
    rates = data["rates"]

    if base == 'USD':
        result1 = amount * rates['KGS']
        print(f"{result1} KGS")
    elif base == 'EUR':
        result = amount * rates['RUB']
        print(f"{result} RUB")

    n = input("Do you wanna to stop(y/n) :")
    if n.lower() == 'y':
        break
    else : continue


 # don't know how to get a data
number = int(input("Enter any number: "))
url = f"http://numbersapi.com/{number}"
response = requests.get(url)

if response.status_code == 200:
    data = response.text
    print(data)


url = f"https://24.kg"
response = requests.get(url)
data = response.text
print(data)




