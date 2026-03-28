# how built an email validation

email = input("Enter your email :")

index = email.index("@")
check = "@gmail.com"

username = email[:index]
domain = email[index:]
if check == domain:
    print(f"Your username is <{username}> and your domain is <{domain}>")
else :
    print("Please enter correct domain")
