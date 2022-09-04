import random
user_wins = 0
computer_wins = 0
values = ["r", "p", "s"]
print("Welcome to Rock/Paper/Scissors game.\nYou'll be playing agaisnt Computer.\nLet's begin!!")
while True:
    user_input = input(
        "\nType your response - Rock(R), Paper(P),Scissors(S) or Quit(Q): ").lower()
    if user_input == "q":
        break
    if user_input not in values:
        print("Please enter correct value - R, P, S or Q.")
        continue
    random_number = random.randint(0, 2)
    computer_pick = values[random_number]
    if computer_pick == values[0]:
        print("\nComputer picked rock.\n")
    elif computer_pick == values[1]:
        print("\nComputer picked paper.\n")
    else:
        print("\nComputer picked scissors.\n")

    if user_input == "r" and computer_pick == "s":
        print("You win!")
        user_wins += 1

    elif user_input == "p" and computer_pick == "r":
        print("You win!")
        user_wins += 1
    elif user_input == "s" and computer_pick == "p":
        print("You win!")
        user_wins += 1
    elif user_input == computer_pick:
        print("Oh it's a draw.")
    else:
        print("Computers wins!")
        computer_wins += 1
if user_wins == 0 and computer_wins == 0:
    print(" ")
else:
    print("\nYou won", user_wins, "times.")
    print("Computer won", computer_wins, "times.")
    if user_wins > computer_wins:
        print("You won by", user_wins - computer_wins, "rounds.")

    elif user_wins == computer_wins:
        print("Oh, it's a draw.")
    else:
        print("Computer wins by", computer_wins - user_wins, "rounds.")
print("Goodbye! Thanks for playing.\n")
input("Press any key to exit.")
