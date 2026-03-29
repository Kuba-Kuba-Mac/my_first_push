import random

options = ("rock","paper","scissor")
playing = True
while playing:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a choice (rock, paper, scissor)? :")

    print(f"Players :{player} ")
    print(f"Computer :{computer}")

    n = input("Would you continue? (y/n) :")
    if n.lower() == "y":
        playing = False



