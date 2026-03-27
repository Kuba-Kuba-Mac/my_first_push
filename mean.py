operator = input("Choose your operation (* + - /) : ")
num1 = float(input("Enter your first number :"))
num2 = float(input("Enter your second number :"))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else :
    print(f"{operator} is not valid")

