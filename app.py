import random

def rock_paper_scissors():
    player_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        possible_choices = ["rock", "paper", "scissors"]

        if user_choice not in possible_choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(possible_choices)
        print(f"\nComputer chose {computer_choice}.\n")

        if user_choice == computer_choice:
            print(f"It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You won!")
            player_score += 1
        else:
            print("You lost.")
            computer_score += 1

        print(f"\nYour score: {player_score}")
        print(f"Computer's score: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

rock_paper_scissors()
