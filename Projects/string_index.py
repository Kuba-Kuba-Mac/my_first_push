# string index how to work and how to use
#
# [start : end : step ]
credit_umber  = "1234-5678-9012-3456"
print(credit_umber[0])
print(credit_umber[:4])
print(credit_umber[5:9])
print(credit_umber[5:])
print(credit_umber[-1])
print(credit_umber[::3])
print(credit_umber[3::])
print(credit_umber[-4:])

print("Chose what do u want to do ?")
print("chose 1 - output one number ")
print("chose 2 - last three number of your credit number")
print("chose 3 - output numbers between a,b numbers ")
n = int(input("Chose your option (1 || 2 || 3) :"))
credit_number  = "1234-5678-9012-3456"
credit_number  = credit_number.replace("-","")
if n == 1:
    m = int(input("Enter which number do you what in credit_number? :"))
    m -=1
    print(credit_number[m])
elif n == 3:
    a = int(input("what is first number in credit_number? :"))
    b = int(input("what is second number in credit_number? :"))
    a -= 1
    print(credit_number[a:b])
elif n == 2:
    print(f"That is your last three number in your credit card {credit_number[-3:]}")
else :
    print("You put wrong number we doesn't have that option")







