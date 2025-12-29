import random
print("=== Welcome to the Dice Rolling Race! ===")
print("You and the computer will roll a die 5 times. Highest total wins!\n")

# Initialize scores
player_total = 0
computer_total = 0
rounds = 5  # Number of rounds

# Loop through rounds
for round_num in range(1, rounds + 1):
    print(f"--- Round {round_num} ---")
    
    # Player rolls
    input("Press Enter to roll your die...")
    player_roll = random.randint(1, 6)
    print(f"You rolled: {player_roll}")
    player_total += player_roll
    
    # Computer rolls
    computer_roll = random.randint(1, 6)
    print(f"Computer rolled: {computer_roll}")
    computer_total += computer_roll
    
    # Show current score
    print(f"Current Score -> You: {player_total} | Computer: {computer_total}\n")

# Determine winner using conditional statements
if player_total > computer_total:
    print("🎉 You win the Dice Race! Congratulations!")
elif player_total < computer_total:
    print("😢 Computer wins this time. Better luck next race!")
else:
    print("🤝 It's a tie! What a close race!")

print("Thanks for playing the Dice Rolling Race! 🏁")
