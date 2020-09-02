import random

win = False
randomNum = None

def giveHint(guess):
    if guess < randomNum:
        print("The number is higher.")
    elif guess > randomNum:
        print("The number is lower.")

print("Welcome to the number guesser")
limit = input("Please enter a limit: ")

if int(limit) <=0:
    limit = input("Please enter a limit higher than 0: ")
else: 
    print("I'm thinking of a number between 0 and", limit)
    randomNum = random.randint(0, int(limit))
    #print(randomNum)

    while win is not True:
        user_input = input("Your guess: ")
        if user_input == None: 
            print("Please try again")
        elif int(user_input) == randomNum:
            win = True
            print("You got the right number. Yeah!!\n")
        else:
            giveHint(int(user_input))
    
