# temperature project
unit  =  input("Is this temperature in Celsius or Fahrenheit (C / F) :")
temp = float(input("Enter the temperature :"))

if unit == "c":
    temp = round((9 * temp) / 5 + 32 ,1)
    print(f"the temperature in Fahrenheit is {temp}F")
elif unit == "f":
    temp = round((temp-32) * 5 / 9 ,1)
    print(f"the temperature in Celsius is {temp}c")
else :
    print(f"{unit} is an invalid unit of measurement")


num =  int(input("Enter a number :"))
print("Positive" if num >= 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"
print(result)
a = int(input("Enter a number :"))
b = int(input("Enter b number :"))
c = int(input("Enter c number :"))

m = a if a > b else b
print(f"max of this numbers is {m}")

weather  = int(input("Enter a temp :"))
result  = "Cold" if not weather >= 18 else "hot"
print(result)
