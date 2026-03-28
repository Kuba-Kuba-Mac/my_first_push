# while_loop
name= input("Enter your name :")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name :")

print(f"hello {name}")

age = int(input("Enter your age :"))

while age < 0:
    print("Age can't be negative ")
    age = int(input("Enter your age :"))
print("ohh you are adult " if age >= 18 else "you are still child")


food = input("Enter a food you like (q to quit) :")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit) :")
print("the operation is quiet")

num  = int(input("Enter number between ( 1 - 10 ): "))

while not num >=1 or num < 11:
    print(f"Your number is {num} ")
    num = int(input("Enter number between ( 1 - 10 ): "))
print("you chose vialence ")



