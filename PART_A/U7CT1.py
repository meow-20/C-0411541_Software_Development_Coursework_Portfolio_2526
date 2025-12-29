import random

def generate_number(start=1, end=100):
    """Generate a random number between start and end."""
    return random.randint(start, end)

def get_guess():
    """Prompt the user to enter a guess and return it as an integer."""
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("❌ Invalid input. Please enter an integer.")

def play_game(max_attempts=5):
    """Main function to play the Guess the Number game."""
    number_to_guess = generate_number()
    attempts = 0
    print(f"🎯 Welcome to 'Guess the Number'! You have {max_attempts} attempts.\n")
    
    while attempts < max_attempts:
        guess = get_guess()
        attempts += 1
        
        if guess == number_to_guess:
            print(f"🎉 Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.\n")
            break
        elif guess < number_to_guess:
            print("⬆️ Too low! Try again.")
        else:
            print("⬇️ Too high! Try again.")
        
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"You have {remaining_attempts} attempts remaining.\n")
        else:
            print(f"💀 Game over! The correct number was {number_to_guess}.\n")

def main():
    """Run the game and ask the user if they want to play again."""
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("👋 Thanks for playing! Goodbye.")
            break
        print()

if __name__ == "__main__":
    main()
