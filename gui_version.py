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
        
    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result.config(text="Invalid input. Please enter an integer.")
            return
        
        self.guess_count += 1
        
        if guess == self.number_to_guess:
            self.result.config(text="Congratulations! You've guessed the number!")
            self.entry.config(state='disabled')
            self.SubmitButton.config(state='disabled')
            self.end_game()
        elif guess < self.number_to_guess:
            self.result.config(text= "Your guess is too low. Try again!")   
        else:
            self.result.config(text="Your guess is too high. Try again!")   
            
        if self.guess_count >= self.max_guesses and guess != self.number_to_guess:
            self.result.config(text=f"Sorry, you've used all attempts. The number was {self.number_to_guess}.")
            self.entry.config(state='disabled')
            self.SubmitButton.config(state='disabled')
            self.end_game()
            
        def end_game(self):
            self.ResetButton.pack(pady=10)
            self.entry.pack_forget() 
            self.SubmitButton.pack_forget()
            self.result.pack(pady=10)
            
        def reset_game(self):
            self.number_to_guess = random.randint(1, 10)
            self.guess_count = 0
            
            self.entry.config(state='normal')
            self.entry.delete(0, tk.END)
            self.result.config(text="")
            
            self.entry.pack(pady=10)
            self.SubmitButton.pack(pady=10)
            self.ResetButton.pack_forget()
            
    if __name__ == "__main__":
        game = NumberGuessingGame()
        game.entry.pack(pady=10)
        game.SubmitButton.pack(pady=10)
        game.result.pack(pady=10)
        game.mainloop()