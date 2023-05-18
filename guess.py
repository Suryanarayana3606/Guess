import random as r
import os
num=r.randrange(1,101)

def game():
    print("Welcome to the NUMBER GUESSING game...")
    print("Guess the number between 1 and 100.")
    choose = input("Choose the level, 'easy' or 'hard' : ").lower()

    is_game=True
    if choose == 'easy':
        while is_game:
            for routine in range(-10,0):           
                print(f"You have only {routine*-1} attempts")
                
                guess = int(input("Make a guess : "))
                
                if num > guess :
                    print("Too low")
                elif num < guess:
                    print("Too high.")
                else:
                    print("You won.")
                    is_game=False
            print("You lost your chances...")
            is_game=False

    if choose == 'hard':
        while is_game:
            for routine in range(-5,0):           
                print(f"You have only {routine*-1} attempts")
                
                guess = int(input("Make a guess : "))
                
                if num > guess :
                    print("Too low")
                elif num < guess:
                    print("Too high.")
                else:
                    print("You won.")
                    is_game=False
            print("You lost your chances...")
            is_game=False
game()
print("You need to play again")
cho = input("Type 'y' or 'n' :").lower()
if cho == 'y':
    os.system('cls')
    game()
else:
    os.system("cls")
