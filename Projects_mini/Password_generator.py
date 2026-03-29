import random


# low = 1
# high = 100
#
# option= ("rock","paper","scissor")
# number = random.randint(1,20)
# number = random.random()
# number = random.choice(option)
# cards = ["2","3","4","5","6","7","8","9","10","j","Q","K","A"]
# random.shuffle(cards)
# print(cards)

low =1
high = 9
cnt = 0
cards = ["2","3","4","5","6","7","8","9","10","j","Q","K","A"]
while True:
    n = random.choice(cards)
    cnt +=1
    print(n,end="")

    if cnt == 8:
        break




