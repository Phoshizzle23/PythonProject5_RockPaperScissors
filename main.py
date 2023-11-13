##############################################################################
# Project #3 - Rock, Paper, Scissors
##############################################################################
# The Following is a breakdown of the code:
##############################################################################
# The play_round function takes the user's input as a parameter,
# a randomnumber to represent the computer's pick,
# and compares the user's input with the computer's pick to determine
# the result of the round. It returns 1 if the user wins,
# -1 if the computer wins, and prints the corresponding message.
# The variables user_wins and computer_wins are initialized to 0
# to keep track of the number of wins for the user and the computer.
# The options list contains the valid choices for the user: "rock," "paper," and "scissors."
# The code enters a while loop, which will continue indefinitely until
# the user enters "q" to quit.
# Inside the loop, the user is prompted to enter their choice of
# "rock," "paper," or "scissors" (or "q" to quit).
# The user's input is converted to lowercase using the lower() method.
# If the user enters "q," the loop breaks, and the program continues to the next section.
# If the user's input is not in the options list,
# the loop continues to the next iteration, prompting the user for input again.
# If the user's input is valid, the play_round function is called with
# the user's input as an argument. The returned result is stored in the result variable.
# Depending on the result of the round, the user_wins or computer_wins counter
# is incremented.
# After the loop finishes, the total number of wins for the user and the
# computer is printed, along with a goodbye message.
##############################################################################
import random

def play_round(user_input):
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == computer_pick:
        print("It's a Draw!")
        return 0

    if (
        (user_input == "rock" and computer_pick == "scissors") or
        (user_input == "paper" and computer_pick == "rock") or
        (user_input == "scissors" and computer_pick == "paper")
    ):
        print("You Won!")
        return 1

    print("You Lose!")
    return -1

user_wins = 0
computer_wins = 0
draws = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter: Rock/Paper/Scissors or Q to Quit! ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    result = play_round(user_input)
    if result == 1:
        user_wins += 1
    elif result == 0:
        draws += 1
    else:
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("There were", draws, "draws.")
print("Goodbye! Thanks for playing!")

