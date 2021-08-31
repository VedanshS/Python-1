import random

print("Number guessing game")

num = random.randint(1, 7)
chances = 5

print("Guess a number (Between 1 and 7):")

while chances > 1:

    guess = int(input("Enter your guess:- "))

    if guess == num:
        print("Congratulation YOU WON!!!")
        
    elif guess < num:
        print("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)

    chances -= 1

while chances == 1:
    if guess == num:
        print("Congratulation YOU WON!!!")
    else : 
        chances -= 1


if chances == 0:
    print("YOU LOSE ! The number was", num)