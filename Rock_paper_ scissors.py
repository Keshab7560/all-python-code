import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Main function to play the game
def play_game():
    choices = ["rock", "paper", "scissors"]
    
    # Get player's choice
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    # Validate player's choice
    if player_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return
    
    # Get computer's choice
    computer_choice = random.choice(choices)
    
    # Print both choices
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {player_choice}")
    
    # Determine the winner
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Start the game
if __name__ == "__main__":
    play_game()
