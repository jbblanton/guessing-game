"""A number-guessing game."""
import random

user_name = input("What is your name?")
print(f"Hello, {user_name}! We're going to play a guessing game!")
print("\n")

number = random.randint(1, 101)
count = 0
winner = False
while winner is False:
    try:
        guess = int(input("Pick a number between 1 & 100: "))
    except ValueError as err:
        print(f"Hello? {user_name}? We're asking for a NUMBER here.")
    else:        
        count += 1
        if guess > 100 or guess < 1:
            print(f"Learn to read, {user_name}; it's gotta be BETWEEN 1 and 100!")
        elif guess == number:
            print(f"Whoa, {user_name}! You guessed correctly in {count} tries!")
            print("\n")
            retry = input("Would you like to play again, and try for a better score? Y/N: ")
                if retry == 'Y':
                    winner = False
                else: 
                    winner = True
        elif guess > number:
            print("Too high, try a lower number.")
        else:
            print("Too low, guess higher!")


    

