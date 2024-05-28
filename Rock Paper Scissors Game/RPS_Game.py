import random

print("This is a Rock, Paper, Scissors game.\n\n")
print("press 1 for Rock")
print("press 2 for Paper")
print("press 3 for Scissors\n\n")

user_choice = int(input("Enter your choice: "))

computer_choice = random.randint(1, 3)

if user_choice == 0:
    print("Invalid choice. Please try again.")      
elif user_choice == 1:
    if computer_choice == 1:
        print("You chose: Rock")
        print("Computer chose: Rock")
        print("It's a tie!")
    elif computer_choice == 2:
        print("You chose: Rock")
        print("Computer chose: Paper")
        print("You lose!")
    elif computer_choice == 3:
        print("You chose: Rock")
        print("Computer chose: Scissors")
        print("You win!")
        
if user_choice == 2:
    if computer_choice == 1:
        print("You chose: Paper")
        print("Computer chose: Rock")
        print("You win!")
    elif computer_choice == 2:
        print("You chose: Paper")
        print("Computer chose: Paper")
        print("It's a tie!")
    elif computer_choice == 3:
        print("You chose: Paper")
        print("Computer chose: Scissors")
        print("You lose!")
        
if user_choice == 3:
    if computer_choice == 1:
        print("You chose: Scissors")
        print("Computer chose: Rock")
        print("You lose!")
    elif computer_choice == 2:
        print("You chose: Scissors")
        print("Computer chose: Paper")
        print("You win!")
    elif computer_choice == 3:
        print("You chose: Scissors")
        print("Computer chose: Scissors")
        print("It's a tie!")