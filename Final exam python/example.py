# import tkinter as tk
# import random

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")

       
        self.lower_bound = 1
        self.upper_bound = 100
        self.guess = None
        
   
        self.label = tk.Label(master, text="Computer's guess:")
        self.label.pack(pady=10)

        self.guess_label = tk.Label(master, text="")
        self.guess_label.pack(pady=10)

        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack(pady=10)

       
        self.too_small_button = tk.Button(self.buttons_frame, text="Too small", command=self.too_small)
        self.too_small_button.pack(side=tk.LEFT, padx=5)

        self.too_large_button = tk.Button(self.buttons_frame, text="Too large", command=self.too_large)
        self.too_large_button.pack(side=tk.LEFT, padx=5)

        self.correct_button = tk.Button(self.buttons_frame, text="Correct", command=self.correct)
        self.correct_button.pack(side=tk.LEFT, padx=5)

        self.new_game_button = tk.Button(master, text="New Game", command=self.new_game)
        self.new_game_button.pack(pady=20)

        self.too_small_button.config(state=tk.DISABLED)
        self.too_large_button.config(state=tk.DISABLED)
        self.correct_button.config(state=tk.DISABLED)
        self.new_game_button.config(state=tk.DISABLED)

        
        self.new_game()

    def new_game(self):
      
        self.target_number = None
        self.lower_bound = 1
        self.upper_bound = 100
        self.guess = None
        self.guess_label.config(text="")
        self.too_small_button.config(state=tk.NORMAL)
        self.too_large_button.config(state=tk.NORMAL)
        self.correct_button.config(state=tk.NORMAL)
        self.new_game_button.config(state=tk.DISABLED)
        self.make_guess()

    def make_guess(self):
        
        self.guess = (self.lower_bound + self.upper_bound) // 2
        self.guess_label.config(text=str(self.guess))  

    def too_small(self):
   
        self.lower_bound = self.guess + 1
        self.make_guess()  

    def too_large(self):
       
        self.upper_bound = self.guess - 1
        self.make_guess()  

    def correct(self):
     
        self.guess_label.config(text=f"Correct! The number was {self.guess}.")
      
        self.too_small_button.config(state=tk.DISABLED)
        self.too_large_button.config(state=tk.DISABLED)
        self.correct_button.config(state=tk.DISABLED)
        self.new_game_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()
