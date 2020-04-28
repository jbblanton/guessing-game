"""A number-guessing game."""
import random

user_name = input("What is your name?")
print(f"Hello, {user_name}! We're going to play a guessing game!")
print("\n")

number = random.randint(1, 101)
count = 0
winner = False
while winner is False:
    #print("Need a number")
    guess = int(input("Pick a number between 1 & 100: "))
    count += 1
    if guess == number:
        print(f"Whoa, {user_name}! You guessed correctly in {count} tries!")
        winner = True
    elif guess > number:
        print("Too high, try a lower number.")
    else:
        print("Too low, guess higher!")
    

