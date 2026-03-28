# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter your food (put q for quiet) :")
    if food.lower() == "q":
        break
    else :
        price = float(input(f"Enter e price of a {food} $:"))
        foods.append(food)
        prices.append(price)

print("-------Your Cart --------")
for i in foods:
    print(i, end= " ")
print()
print(f"Your total is {round(sum(prices),2)}$")