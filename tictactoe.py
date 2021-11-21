from time import sleep
from random import randrange

WIDTH = 50

def main_menu():
    choice = ""
    while choice != "Q":
        choice = menu("TIC TAC TOE", ["P - PLAY A GAME", "A - ABOUT", "Q - QUIT"], "press choice then ENTER: ").upper()
        if choice == "P":
            select_difficulty()
        elif choice == "A":
            about()
        else:
            print(center_padding("PLEASE SELECT A VALID OPTION"))


def select_difficulty():
    choice = ""
    while choice != "B":
        difficulty = menu("SELECT DIFFICULTY", ["E - EASY", "M - MEDIUM", "D - DIFFICULT", "B - BACK TO MAIN MENU"], "press choice then ENTER: ").upper()
        if difficulty == "E" or difficulty == "M" or difficulty == "D":
            play_game(difficulty)

        
def play_game(difficulty):
    gameboard = {1 : "1",  2 : "2",  3 : "3", 4 : "4",  5 : "5",  6 : "6", 7 : "7",  8 : "8",  9 : "9"}
    for turn in range(9):
        if turn % 2 == 0:
            player = "PLAYER"
            print("PLAYER'S TURN")
            gameboard = player_turn(gameboard)
        else:
            player = "COMPUTER"
            print("COMPUTER'S TURN")
            gameboard = computer_turn(gameboard, difficulty, turn)
        if check_winner(gameboard):
            print("winner found")
            break
        # change whose turn it is
        turn += 1
    print_board(gameboard)
    if turn < 9:
        print(f"WINNER: {player}")
    else:
        print("DRAW")
    print("game over")


def player_turn(gameboard):
    print_board(gameboard)
    valid_choice = False
    while not valid_choice:
        choice = input("enter square number: ")
        if choice.isdigit() and int(choice) > 0 and int(choice) < 10:
            try:
                if int(choice) == int(gameboard[int(choice)]):
                    valid_choice = True
                    gameboard[int(choice)] = "X"
            except:
                print(f"SQUARE {choice} HAS ALREADY BEEN PLAYED")
        else:
            print("ENTER A VALID SQUARE, 1-9")
    return gameboard


def computer_turn(gameboard, difficulty, turn):
    
    print("Checking potential wins")
    complete = fill_in_third_blank(gameboard, "O")
    
    if not complete and "D" in difficulty and turn == 1:
        print("Proactive D)")
        # D is "PROACTIVE" - it tries to disrupt winning strategies preemptively
        if gameboard[5].isdigit():
            gameboard[5] = "O"
            complete = True
        else:
            square = randrange(4)
            if square == 0:
                gameboard[1] = "O"
            elif square == 1:
                gameboard[3] = "O"
            elif square == 2:
                gameboard[7] = "O"
            elif square == 3:
                gameboard[9] = "O"
            complete = True
    
    if not complete and "E" not in difficulty:
        print("Reactive M")
        # M is "REACTIVE" - it tries to stop the player from getting 3 in a row
        complete = fill_in_third_blank(gameboard, "X")
        
    if not complete and "D" in difficulty:
        print("Anticipating D")
        if gameboard[5] == "O":
            # tries to anticipate player winning sequences and disrupt them
            complete = fill_in_difficult_sequences(gameboard, "X")

        if not complete:
            # tries to set up own winning sequences
            complete = fill_in_difficult_sequences(gameboard, "O")
            pass 

    # if not complete:
    #     print("Independent E")
    #     # E is "INDEPENDENT" - it tries to complete its own 3-in-a-row
    #     complete = fill_in_second_blank(gameboard)
    
    while not complete:
        # If none of the above methods are working, it will pick a square at random
        print("ATTEMPTING E")
        choice = randrange(1,10)
        if gameboard[choice].isdigit():
            gameboard[choice] = "O"
            complete = True
    return gameboard


def fill_in_third_blank(gameboard, watch_variable):
    winning_sequences = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for sequence in winning_sequences:
        match_ratio = 0
        for s in sequence:
            if gameboard[s] == watch_variable:
                match_ratio += 1
        if match_ratio == 2:
            for s in sequence:
                if gameboard[s].isdigit():
                    gameboard[s] = "O"
                    return True
    return False


def fill_in_difficult_sequences(gameboard, watch_variable):
    difficult_sequences = [[1, 9, 2], [3, 7, 6], [1, 6, 3], [1, 8, 7], [3, 4, 1],[3, 8, 9], [7, 2, 1], [7, 6, 9], [9, 4, 7], [9, 2, 3]]
    for sequence in difficult_sequences:
        if gameboard[sequence[0]] == watch_variable and gameboard[sequence[1]] == watch_variable and gameboard[sequence[2]].isdigit():
            gameboard[sequence[2]] = "O"
            return True
    return False


def fill_in_second_blank(gameboard):
    winning_sequences = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for sequence in winning_sequences:
        if gameboard[sequence[0]] == "O":
            if gameboard[sequence[1]].isdigit() and gameboard[sequence[2]].isdigit():
                flip = randrange(2)
                gameboard[sequence[1]] = "O"
                gameboard[sequence[1] if flip == 0 else sequence[2]]
                return True
    return False


def coin_flip(heads, tails):
    flip = randrange(2)
    return heads if flip == 0 else tails


def check_winner(gameboard):
    winning_sequences = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for sequence in winning_sequences:
        if gameboard[sequence[0]] == gameboard[sequence[1]] == gameboard[sequence[2]]:
            return True
    return False


# add an about section
def about():
    pass


# *****************************************************************************************************
#       Formatting and Display Section below
# *****************************************************************************************************


full_spacer = "**************************************************"
empty_spacer = "*                                                *"


def menu(title, content, prompt):
    height = 10
    while height > 0:
        if height == 10 or height == 2:
            print(full_spacer)
        elif height == 9:
            print(center_padding(title))
        elif height == 8:
            print(empty_spacer)
        elif height == 7:
            for line in content:
                print(left_padding(line))
                height -= 1
        elif height < 8 and height > 3:
            print(empty_spacer)
        elif height == 1:
            choice = input(prompt)
        height -= 1
    print("\n\n")
    return choice


def center_padding(content):
    while len(content) < WIDTH - 2:
        if len(content)%2 == 0:
            content = content + " "
        else:
            content = " " + content
    return "*" + content + "*"


def left_padding(content):
    content = "* " + content
    while len(content) < WIDTH - 1:
        content = content + " "
    return content + "*"


def print_board(gameboard):
    border = "***************"
    number = "*  {0} | {1} | {2}  *"
    line   = "* ---+---+--- *"
    print(border)
    print(number.format(gameboard[1],gameboard[2],gameboard[3]))
    print(line)
    print(number.format(gameboard[4],gameboard[5],gameboard[6]))
    print(line)
    print(number.format(gameboard[7],gameboard[8],gameboard[9]))
    print(border)


main_menu()
