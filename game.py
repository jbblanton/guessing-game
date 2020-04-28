"""A number-guessing game."""
import random

user_name = input("What is your name?")
print(f"Hello, {user_name}! We're going to play a guessing game!")
print("\n")


low_num = int(input("What is our low number?"))
up_num = int(input("What is our high number?"))
number = random.randrange(low_num, up_num + 1)
count = 0

winner = False
while winner is False:
    try:
        guess = int(input(f"Pick a number between {low_num} & {up_num}: "))
    except ValueError as err:
        print(f"Hello? {user_name}? We're asking for a NUMBER here.")
    else:        
        count += 1
        if count == 5:
            print(f"Sorry, {user_name}, you didn't guess fast enough. Better luck next time!")
            winner = True
        
        elif guess > up_num or guess < low_num:
            print(f"Learn to read, {user_name}; it's gotta be BETWEEN {low_num} and {up_num}!")
        
        elif guess == number:
            print(f"Whoa, {user_name}! You guessed correctly in {count} tries!")
            winner = True
        
        elif guess > number:
            print("Too high, try a lower number.")
        
        else:
            print("Too low, guess higher!")


    

