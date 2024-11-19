# # Register players
# player1_name = input("Register 1st player name as ID: ")
# player2_name = input("Register 2nd player name as ID: ")

# # Initialize scores
# player1_score = 0
# player2_score = 0

# # Print game rules
# print("Now read game rules.\n")
# print("snake = 1")
# print("water = 2")
# print("gun = 3\n")

# # Choices for snake, water, gun
# snake = 1
# water = 2
# gun = 3

# # Define a function for a single round
# def play_round(round_number):
#     global player1_score, player2_score  # Access the score variables
#     print(f"\nThis is round {round_number} of the game.\n")

#     player1_choice = int(input(f"Enter a number {player1_name} (1-3): "))
#     player2_choice = int(input(f"Enter a number {player2_name} (1-3): "))

#     if player1_choice == 1 and player2_choice == 2:
#         print(f"{player1_name} wins this round!")
#         player1_score += 1
#     elif player1_choice == 1 and player2_choice == 3:
#         print(f"{player2_name} wins this round!")
#         player2_score += 1
#     elif player1_choice == 2 and player2_choice == 1:
#         print(f"{player2_name} wins this round!")
#         player2_score += 1
#     elif player1_choice == 2 and player2_choice == 3:
#         print(f"{player1_name} wins this round!")
#         player1_score += 1
#     elif player1_choice == 3 and player2_choice == 1:
#         print(f"{player1_name} wins this round!")
#         player1_score += 1
#     elif player1_choice == 3 and player2_choice == 2:
#         print(f"{player2_name} wins this round!")
#         player2_score += 1
#     elif player1_choice == player2_choice:
#         print(f"{player1_name} and {player2_name}, this round is a draw. Play again!")
#     else:
#         raise ValueError("Invalid choice entered.")

# # Play three rounds
# for round_number in range(1, 4):
#     play_round(round_number)

# # Display final scores and winner
# print("\nGame Over!")
# print(f"Final Scores: {player1_name}: {player1_score}, {player2_name}: {player2_score}")
# if player1_score > player2_score:
#     print(f"Congratulations {player1_name}, you are the overall winner!")
# elif player2_score > player1_score:
#     print(f"Congratulations {player2_name}, you are the overall winner!")
# else:
#     print("It's a draw! Both players have equal scores.")

# a = int(input(""))

import random
def check(comp, user):
    if comp == user:
        return 0
    if comp == 0 and user == 1:
        return -1
    if comp == 1 and user == 2:
        return -1
    if comp == 2 and user == 1:
        return -1
    
comp = random.randint(0, 2)
user = int(input("0 for snake, 1 for water, and 2 for gun: "))
score = check(comp, user)
print("You:", user)
print("computer:", comp)
if score == 0:
    print("Its draw. Play again.")
elif score == -1:
    print("You lose. Computer win.")
else:
    print("You win. Computer loss.")