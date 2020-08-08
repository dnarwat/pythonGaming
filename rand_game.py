import random
number = random.randint(1, 10)
uname = input("enter your username: ")
print("Hello", uname, ".")
tries = 1
ques = input("wanna play a game?[y/n]")

if ques == "n":
    print("oh okay..")
if ques == "y":
    print("i am thinking of a number from 1 to 10.")
    guess = int(input("have a guess:"))
    if guess < number:
        print("guess higher")
    if guess > number:
        print("guess lower")
    while guess != number:
        tries += 1
        guess = int(input("try again"))
        if guess < number:
            print("guess higher")
        if guess > number:
            print("guess lower")
    if guess == number:
        print("you are right. the number was ", number, "and it took ", tries, "tries")