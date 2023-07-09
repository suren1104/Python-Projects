import random

number = random.randint(1, 99)
guess = int(input("Enter an integer from 1 to 99: "))
while number != guess:
    if guess < number:
        print("Guess is low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > number:
        print("Guess is high")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        break
print("You guessed it!")
