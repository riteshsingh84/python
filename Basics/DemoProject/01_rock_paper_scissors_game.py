# Description: A simple rock-paper-scissors game where the user plays against the computer.

import random

choices = ['rock', 'paper', 'scissors']

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(choices)   

def get_user_choice():
    """Get the user's choice of rock, paper, or scissors."""
    while True:
        user_input = input("Enter rock, paper, or scissors: ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please try again.")  

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
    
def play_game():
    """Main function to play the rock-paper-scissors game."""
    print("Welcome to Rock-Paper-Scissors!")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)   

if __name__ == "__main__":
    play_game() 