import random

options = ['Rock', 'Paper', 'Scissors']
user_score = 0
computer_score = 0

rounds = int(input("How many rounds do you want to play? "))

for i in range(rounds):
    choice = random.choice(options)
    user_input = input("Choose Rock, Paper, or Scissors (capitalize first letter): ")
    print("Random choice:", choice)

    if user_input == choice:
        print("It's a tie!")
    elif user_input == "Rock" and choice == "Scissors":
        print("You win!")
        user_score += 1
    elif user_input == "Scissors" and choice == "Rock":
        print("You lose!")
        computer_score += 1
    elif user_input == "Paper" and choice == "Rock":
        print("You win!")
        user_score += 1
    elif user_input == "Rock" and choice == "Paper":
        print("You lose!")
        computer_score += 1
    elif user_input == "Scissors" and choice == "Paper":
        print("You win!")
        user_score += 1
    elif user_input == "Paper" and choice == "Scissors":
        print("You lose!")
        computer_score += 1
    print("Score: You", user_score, "Computer", computer_score)
    print()

if user_score > computer_score:
    print("You won the game! Final Score:", user_score, "Computer:", computer_score)
elif computer_score > user_score:
    print("You lost the game! Final Score:", user_score, "Computer:", computer_score)
else:
    print("It's a tie! Final Score:", user_score, "Computer:", computer_score)