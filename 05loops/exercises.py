# EX 1 - menu

user_option = 0

while user_option != 3:
    print("Select an option: ")
    print("1. - Create account")
    print("2. - Delete account")
    print("3. - Exit ")

    user_option = int(input())

    if user_option == 1:
        print("Creating...")
    elif user_option == 2:
        print("Deleting account...")
    else:
        print("Exit...")

# EX 2 - ATM

user_option = 0
balance = 1000

while user_option != 4:
    print("Select an option: ")
    print("1. - Check balance")
    print("2. - withdraw balance")
    print("3. - Enter balance")
    print("4. - Exit")

    user_option = int(input())

    if user_option == 1:
        print(f"Amount: {balance}")
    elif user_option == 2:
        userAmount = float(input("Amount: "))
        balance = (balance - userAmount) if (balance - userAmount >= 0) else balance 
    elif user_option == 3:
        userAmount = float(input("Amount: "))
        balance += userAmount

print("Thank you !")


# EX 3 - Guess Number
import random

MAX_TRY = 7
GUESS_NUMBER = random.randint(0, 100)
current_try = 0
user_winner = False

while current_try < MAX_TRY and not user_winner :
    userNumber = int(input("Your number: "))

    if userNumber < GUESS_NUMBER:
        print(f"Your number is more less... try: {current_try + 1}")
    elif userNumber > GUESS_NUMBER:
        print(f"Your number is more biggest... {current_try + 1}")
    else:
        print("Congrats !!")
        user_winner = True
    
    current_try+=1

if not user_winner:
    print("You lose :'( ")

# Ex 4 - An valid user name

user_name = None

while not user_name:
    user_name = input("Your user name: ")

print(user_name)