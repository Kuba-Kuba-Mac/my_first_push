def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


result = is_prime(3)
if result:
    print("Yes, it is a prime number")
else:
    print("No, it isn't")