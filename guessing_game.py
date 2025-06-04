"""Number guessing game"""

import random

def play_number_guessing_game():
    """
    Play a number guessing game where the user has
    three attempts to guess a randomly selected
    number between 1 and 10.
    """
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 10.")
    number_to_guess = random.randint(1, 10)

    for guess_count in range(3):
        guess = input(f"Attempt {guess_count + 1}: Please enter your guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            break
        if guess < number_to_guess:
            print("Your guess is too low. Try again!")
        else:
            print("Your guess is too high. Try again!")
    else:
        print(f"Sorry, you've used all attempts. The number was {number_to_guess}.")

# Main game loop
while True:
    play_number_guessing_game()
    answer = input("Do you want to play again? (yes/no): ").strip().lower()
    if answer == "no":
        print("Thanks for playing! Goodbye!")
        break
