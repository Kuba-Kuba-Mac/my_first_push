import time

n = int(input("Enter the time n second :"))
for x in range(n,0,-1):
    second = x % 60
    minutes = int((x / 60) % 60)
    hour = int(x/3600) % 24
    print(f"{hour:02}:{minutes:02}:{second:02}")
    time.sleep(1)

print("Time's Up")