"""Number Guessing Game GUI version"""
import tkinter as tk
import random

class NumberGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Guessing Game")
        self.geometry("400x300")
        self.configure(bg="lightgreen")

        self.number_to_guess = random.randint(1, 10)
        self.guess_count = 0
        self.max_guesses = 3
        
        self.label = tk.Label(self, text="Guess a number between 1 and 10:", font=("Arial", 14), bg="white")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self, font=("Arial", 14))
        self.result = tk.Label(self, text="", font=("Arial", 14), bg="white")
        self.SubmitButton = tk.Button(self, text="Submit Guess", command=self.check_guess, font=("Arial", 14), bg="lightblue")
        self.ResetButton = tk.Button(self, text="Play Again", command=self.reset_game, font=("Arial", 14), bg="lightblue")
        
        

