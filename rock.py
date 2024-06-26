'''User Input: Prompt the user to choose rock, paper, or scissors.

Computer Selection: Generate a random choice (rock, paper, or scissors) for

the computer.

Game Logic: Determine the winner based on the user's choice and the

computer's choice.

Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.

Display the result, whether the user wins, loses, or it's a tie.

Score Tracking (Optional): Keep track of the user's and computer's scores for

multiple rounds.

Play Again: Ask the user if they want to play another round.

User Interface: Design a user-friendly interface with clear instructions and

feedback.'''
import random
user_action=input("Enter a choice(paper,rock,scissors):")
possible_actions = ["rock", "paper", "scissors"]
computer_action=random.choice(possible_actions)
print(f"\nyou chose{user_action},computer chose{computer_action}.\n")
if user_action==computer_action:
    print(f"both players selected{user_action}.it's a tie!")
elif user_action=="paper":
    if computer_action=="scissors":
        print("paper smashes scissors! you win!")
    else:
        print("rock smashes scissors! you win!")
elif user_action=="rock":
    if computer_action=="rock":
        import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

