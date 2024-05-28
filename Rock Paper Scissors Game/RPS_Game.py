import random

def get_user_choice():
    while True:
        try:
            print("\nChoose your weapon:")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "You lose!"

def display_choices(user_choice, computer_choice):
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"\nYou chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

def display_ascii(choice):
    rock = "    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)"
    paper = "    _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)"
    scissors = "    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"
    choices = {1: rock, 2: paper, 3: scissors}
    print(choices[choice])

def main():
    print("Welcome to Rock, Paper, Scissors!\n")
    rounds = int(input("How many rounds do you want to play? "))
    user_score = 0
    computer_score = 0
    for round in range(1, rounds + 1):
        print(f"\nRound {round}:")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        display_choices(user_choice, computer_choice)
        display_ascii(user_choice)
        display_ascii(computer_choice)
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1
    print("\nGame Over!")
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You win the game!")
    elif user_score < computer_score:
        print("Sorry, you lost the game.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
