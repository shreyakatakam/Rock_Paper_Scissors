import random
import tkinter as tk
from tkinter import messagebox

def play_game(user_choice):
    device_choice = random.randint(1, 3)
    choices = ["Rock", "Scissors", "Paper"]
    device_input_choice = choices[device_choice - 1]

    if user_choice == device_input_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and device_input_choice == "Scissors") or \
         (user_choice == "Scissors" and device_input_choice == "Paper") or \
         (user_choice == "Paper" and device_input_choice == "Rock"):
        result = "You Win!"
    else:
        result = "You Lose!"

    messagebox.showinfo("Result", f"Device has selected {device_input_choice}\n{result}")

def play_again():
    choice = messagebox.askyesno("Play Again", "Would you like to play again?")
    if choice:
        rock_button.config(state=tk.NORMAL)
        paper_button.config(state=tk.NORMAL)
        scissors_button.config(state=tk.NORMAL)
    else:
        root.destroy()

root = tk.Tk()
root.title("Rock Paper Scissors")

rock_button = tk.Button(root, text="Rock", command=lambda: play_game("Rock"))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("Paper"))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("Scissors"))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.grid(row=1, column=1, pady=10)

root.mainloop()
