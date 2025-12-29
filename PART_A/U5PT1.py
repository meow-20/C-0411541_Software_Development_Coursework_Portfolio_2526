import random 
import math  

# Generate a random number between 1 and 50
secret_number = random.randint(1, 50)

print("Welcome to the Number Guessing Game!")
print("Try to guess the secret number between 1 and 50.\n")

# Initialize attempts counter
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    # CONDITIONAL STATEMENTS: Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break  

    elif guess < secret_number:
        print("Too low! Try a higher number.")
        print(f"Hint: The square root of the secret number is approximately {math.sqrt(secret_number):.2f}")

    else:
        print("Too high! Try a lower number.")
        print(f"Hint: The ceiling of half the secret number is {math.ceil(secret_number/2)}")
