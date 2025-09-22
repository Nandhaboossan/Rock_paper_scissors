"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types “quit”.
"""
import random
import sys 
import time
import os
from colorama import Fore, Style, init
init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')
choices = ['rock', 'paper', 'scissors']
player_score = 0    
computer_score = 0
rounds_played = 0
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

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

def display_scores():
    print(Fore.GREEN + f"Player Score: {player_score}" + Style.RESET_ALL)
    print(Fore.RED + f"Computer Score: {computer_score}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Rounds Played: {rounds_played}" + Style.RESET_ALL)
    print("-" * 30)
print_slow("Welcome to Rock, Paper, Scissors!")
print_slow("Type 'rock', 'paper', or 'scissors' to play.")
print_slow("Type 'quit' to exit the game.")
print("-" * 30)

while True:
    player_choice = input("Your choice: ").lower()
    if player_choice == 'r':
        player_choice = 'rock'
    elif player_choice == 'p':
        player_choice = 'paper'
    elif player_choice == 's':
        player_choice = 'scissors'
    if player_choice == 'quit':
        print_slow("Thanks for playing! Final scores:")
        display_scores()
        break
    if player_choice not in choices:
        print_slow("Invalid choice. Please try again.")
        continue
    computer_choice = get_computer_choice()
    print_slow(f"Computer chose: {computer_choice}")
    result = determine_winner(player_choice, computer_choice)
    rounds_played += 1
    print_slow(result)
    display_scores()
