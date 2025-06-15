# This demo project is a simple dice game where the user can roll a die and see the result.
import random
# Description: A simple dice game where the user can roll a die and see the result.
# This uses the random module to simulate rolling a die.
# It prompts the user to roll the die and displays the result.
# It also allows the user to roll again or exit the game.

def roll_dice():
    """Function to simulate rolling a die."""
    return random.randint(1, 6) # Returns a random integer between 1 and 6, simulating a die roll   

def main():
    """Main function to run the dice game."""
    print("Welcome to the Dice Game!")
    
    do_you_wat_to_play_again = False

    while True:
        if not do_you_wat_to_play_again:
         input("Press Enter to roll the die...")  # Wait for user input to roll the die

        result = roll_dice()  # Call the roll_die function to get the result

        print(f"You rolled a {result}!")  # Print the result of the die roll
        
        play_again = input("Do you want to roll again? (yes/no): ").strip().lower()  # Ask if the user wants to play again

        if play_again == 'no':  # If the user does not want to play again, exit the loop
            print("Thanks for playing! Goodbye!")
            break  # Exit the while loop

        do_you_wat_to_play_again = True  # Set the flag to indicate the user wants to play again

if __name__ == "__main__":
    main()  # Call the main function to start the game