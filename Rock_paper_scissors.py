"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types “quit”.
"""

# --- Tkinter GUI version ---
import random
import tkinter as tk
from tkinter import messagebox

choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0
rounds_played = 0

def get_computer_choice():
    return random.choice(choices)

def determine_winner(player, computer):
    global player_score, computer_score
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        player_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

def play(player_choice):
    global rounds_played
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    rounds_played += 1
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    update_scores()

def update_scores():
    score_label.config(text=f"Player Score: {player_score}\nComputer Score: {computer_score}\nRounds Played: {rounds_played}")

def quit_game():
    messagebox.showinfo("Game Over", f"Thanks for playing!\nFinal scores:\nPlayer: {player_score}\nComputer: {computer_score}\nRounds: {rounds_played}")
    root.destroy()

# --- GUI Setup ---
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("350x300")

welcome_label = tk.Label(root, text="Welcome to Rock, Paper, Scissors!", font=("Arial", 14))
welcome_label.pack(pady=10)

score_label = tk.Label(root, text="Player Score: 0\nComputer Score: 0\nRounds Played: 0", font=("Arial", 12))
score_label.pack(pady=5)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 12))
result_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play('rock'))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play('paper'))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play('scissors'))
scissors_btn.grid(row=0, column=2, padx=5)

quit_btn = tk.Button(root, text="Quit", width=10, command=quit_game)
quit_btn.pack(pady=10)

root.mainloop()
