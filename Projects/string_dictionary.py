 # learning  string method in python
name = input("Enter your name :")

result  = len(name)
result = name.find("a")
result = name.rfind("q") # return -1 if can't find
name = name.capitalize()
name = name.upper()
name = name.lower()
result = name.isdigit()
result = name.isalpha()
result = name.count("-")
result = name.replace("-","")
print(result)


 # some task about validation
name = input("Enter your username :")
if len(name) > 12 :
    print("Your username can't more 12 character ")
elif not name.find(" ") == -1:
    print("Your username can't contain space ")
elif  not name.isalpha():
    print("Your username can't contain a digit ")
else :
    print(f"Your {name} is valid ")



