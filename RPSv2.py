# Made by Flognog
# November 14th 2018
# Found on Github

import random

opponent_names = ["Fluffy","Gritty","Chloe","Sharkie","Cookie and Smalls"]
op_pick = ["R","P","S"]
# Prints welcome and directions

print("\nWelcome To Rock Paper Scissors!")

# Handels Play Again
def playagain():
    while True:
        play_again = str.upper(input("Would you like to play again? Y/N "))
        if play_again == "Y":
            play()
            break
        elif play_again == "N":
            quit()
            break
        else:
            print("Invalid Entry")

# The Game!
def play():
    # winning number
    winning_number = 0

    # Guess Number
    guess_num = 1

    # Finds Random Opponents name
    opponent = str(opponent_names[random.randint(0, 4)])

    print("\nPick: Best of 3, 5 or 7\n")
    length = int(input("Enter: "))

    # Gets the best of the number Ex: best of 3 == 2, best of 5 == 3, best of 7 == 4
    if length == 3:
        winning_number = 2
    elif length == 5:
        winning_number = 3
    elif length == 7:
        winning_number = 4

    ply_wins = 0
    cmp_wins = 0

    # Prints Oppoenent
    print("\nYour Opponent Is " + opponent)

    # Plays the Game
    while True:

        # Prints Directions
        if ply_wins < winning_number and cmp_wins < winning_number:
            print("\nGame " + str(guess_num))
            print("Your Score: " + str(ply_wins) + "\nComputer Score: " + str(cmp_wins))
            print("\nEnter:\nR for Rock\nP for Paper\nS for Scissors\n")
            ply_guess = str.upper(input("Your Pick: "))
            op_guess = str.upper(op_pick[random.randint(0, 2)])

            if ply_guess == "R":
                if op_guess == ply_guess:
                    print(" ")
                    print(opponent + " picked Rock\nRock ties Rock\n")
                    print("Draw\nTry Again\n")

                elif op_guess == "P":
                    print(" ")
                    print(opponent + " picked Paper\nPaper beats Rock\n")
                    print("You Lost the round\n")
                    guess_num = guess_num + 1
                    cmp_wins = cmp_wins +1

                elif op_guess == "S":
                    print(" ")
                    print(opponent + " picked Scissors\nRock beats Scissors\n")
                    print("You Win the round!\n")
                    guess_num = guess_num + 1
                    ply_wins = ply_wins + 1

                else:
                    # Error 001: ply_guess R if Failed
                    print("Critical Error 001")
                    quit()

            elif ply_guess == "P":
                if op_guess == ply_guess:
                    print(" ")
                    print(opponent + " picked Paper\nPaper ties Paper\n")
                    print("Draw\nTry Again\n")

                elif op_guess == "S":
                    print(" ")
                    print(opponent + " picked Scissors\nScissors beats Paper\n")
                    print("You Lost this round\n")
                    guess_num = guess_num + 1
                    cmp_wins = cmp_wins + 1

                elif op_guess == "R":
                    print(" ")
                    print(opponent + " picked Rock\nPaper beats Rock\n")
                    print("You Win this round!\n")
                    guess_num = guess_num + 1
                    ply_wins = ply_wins + 1

                else:
                    # Error 002: ply_guess P if Failed
                    print("Critical Error 002")
                    quit()

            elif ply_guess == "S":
                if op_guess == ply_guess:
                    print(" ")
                    print(opponent + " picked Scissors\nScissors ties Scissors\n")
                    print("Draw\nTry Aging\n")

                elif op_guess == "R":
                    print(" ")
                    print(opponent + " picked Rock\nRock beats Scissors\n")
                    print("You Lost\n")
                    guess_num = guess_num + 1
                    cmp_wins = cmp_wins + 1

                elif op_guess == "P":
                    print(" ")
                    print(opponent + " picked Paper\nScissors beats Paper\n")
                    print("You Win!\n")
                    guess_num = guess_num + 1
                    ply_wins = ply_wins + 1

                else:
                    # Error 003: ply_guess R if Failed
                    print("Critical Error 003")
                    quit()

            else:
                print("Invalid Input")

        elif ply_wins == winning_number:
            print("\nCongrats You WIN!\n\n")
            playagain()

        elif cmp_wins == winning_number:
            print("\nSorry You Lost...\n\n")
            playagain()

        else:
            print("Critical Error")
            quit()

# The Help Page
def help_guide():
    # Directions on how to play
    print("\nHow To Play:\n\nYou Guess either: Paper, Rock, Scissors\nThen the computer randomly selects either: Paper, Rock, Scissors\n\n")
    print("How to Win:\n\nPaper:\nBeats Rock\nLoses to Scissors\nTies Paper\n")
    print("Rock:\nBeats Scissors\nLoses to Paper\nTies Rock\n")
    print("Scissors:\nBeats Paper\nLoses to Rock\nTies Scissors\n")
    print("\nBest Of:\n\nBest of 3: Win 2 rounds to Win\n")
    print("Best of 5: Win 3 rounds to Win\n")
    print("Best of 7: Win 4 rounds to Win\n\n")

    while True:
        # Gets Users input on if they want to return to the main menu
        return_to_menu = str.upper(input("Would you like to return to the Main Menu? Y/N "))
        if return_to_menu == "Y":
            mainmenu()
            break
        elif return_to_menu == "N":
            return_to_menu = str.upper(input("Enter Y when ready to return to the Main Menu: "))
            if return_to_menu == "Y":
                mainmenu()
                break
            else:
                print("Invalid Entry")
        else:
            print("Invalid Entry")

# Asks for users input on if they want to play/quit/help
def mainmenu():
    while True:
        print("\nP for Play\nQ for Quit\nH for Help\n")
        # Gets Users Input
        pqh = str.upper(input("Enter: "))

        if pqh == "P":
            play()
            break
        elif pqh == "H":
            help_guide()
            break
        elif pqh == "Q":
            print("\nSee You Next Time!\n")
            quit()
            break
        else:
            print("Invalid Entry, Please Enter: P for play, Q for Quit, H for Help")


# Starts the Main Menu
mainmenu()