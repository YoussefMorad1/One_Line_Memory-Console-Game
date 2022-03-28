# Author: Youssef Mohammed Morad
# This program is a simple memory game of one line.
# Player chooses 2 coins and if they have the same characters he gets a point and these coins are removed.
# Winner who has more points when all coins are removed
# Version: 1.0 >> Date: 24/02/2022
    # Main algorithm and Game worked
# Version: 1.1 >> Date: 25/02/2022
    # Fixed some wrong input bugs. Made the winner plays again until he makes a mistake. reformatted the code and added comments
# Version: 1.1.1 >> Date: 10/03/2022
    # Deleted a confusing variable and changed some confusing variables' names


def create_num_list(num_of_elems=20):  # Function to create the list of numbers (shown at start)
    global num_list
    num_list = []
    for i in range(0,num_of_elems):
        num_list.append(i + 1)
    return num_list


def create_char_list(num_of_elems=20):  # Function to create the list of characters (but not randomized yet)
    global char_list
    char_list = []
    for i in range(0,num_of_elems//2):
        char_list.append(chr(65+i))
    char_list *= 2
    return char_list


def sort_char_list_randomly(sorted_list):  # Function to make the characters list in random order
    from random import randint
    randomed_list = []
    real_length = len(sorted_list)
    for i in range(real_length):
        modified_length = len(sorted_list)
        random_index = randint(0, modified_length-1)
        randomed_list.append( sorted_list[random_index] )
        sorted_list.pop(random_index)
    return randomed_list


def get_input(num, number_of_elems, last_list):  # Function to take suitable input from user
    while True:
        choices = num.split()
        if len(choices) == 2:
            if choices[0].isdigit() and choices[1].isdigit():
                choices[0] = int(choices[0])
                choices[1] = int(choices[1])
                if choices[0] in range(1, number_of_elems + 1) and choices[1] in range(1, number_of_elems + 1) and (choices[0] != choices[1]) and last_list[choices[0]-1] != '*' and last_list[choices[1]-1] != '*':
                    break
        num = input("Please enter 2 valid numbers separated with space: ")
    return choices


def show_choices(choice1, choice2, last_list, random_list):  # Showing the effect of choosing 2 numbers
    choice1 -= 1
    choice2 -= 1
    shown_list = last_list[:]
    shown_list[choice1] = random_list[choice1]
    shown_list[choice2] = random_list[choice2]
    return shown_list


def clear():  # clear screen after showing the choices
    from os import system, name
    if name == 'nt':
        _ = system('cls') #


def update_list(shown_list, choice1, choice2, player):  # Updating the list to a new version
    global player1_again, player2_again
    player1_again, player2_again = True, True
    new_list = shown_list[:]
    if shown_list[choice1-1] == shown_list[choice2-1]:  # put * * if he got a point
        new_list[choice1-1] = '*'
        new_list[choice2-1] = '*'
        if player == 1:  # increase player_1's score if he got the point and give another turn
            increase_score(1)
            player2_again = False
        else:  # increase player_2's score if he got the point and give another turn
            increase_score(2)
            player1_again = False
    else:  # puts the number again on the chosen characters
        new_list[choice1 - 1] = num_list[choice1-1]
        new_list[choice2 - 1] = num_list[choice2-1]
        player1_again, player2_again = False, False
    return new_list


def increase_score(player_num):  # increase the score of the player who got point
    global score_1, score_2
    if player_num == 1:
        score_1 += 1
    else:
        score_2 += 1
    return None


def found_winner(last_list):  # checks the winner (if the function is full of '*')
    length = len(last_list)
    is_winner = True
    for i in range(length):
        if last_list[i] != '*':
            is_winner = False
            break
    return is_winner


def print_winner():  # prints the scores and the winner or the draw
    print(f'Player 1: {score_1} points')
    print(f'Player 2: {score_2} points')
    print('****************************')
    if score_1 > score_2:
        print(f'The Winner Is Player 1')
    elif score_1 < score_2:
        print(f'The Winner Is Player 2')
    else:
        print("Draw")
    print('****************************')


def One_Line_Memory_Game():  # The main function of the game

    from time import sleep
    global score_1, score_2
    score_1, score_2 = 0, 0
    num_list = create_num_list()
    length = len(num_list)
    char_list = create_char_list()
    random_char_list = sort_char_list_randomly(char_list)
    last_list = num_list[:]
    global player1_again, player2_again

    while True:
        # player_1 turn
        player1_again = True
        while player1_again:
            print(*random_char_list)
            print(*last_list)
            first = input(f'Player#1-Score {score_1}: ')
            first = get_input(first, length, last_list)
            shown_list = show_choices(first[0], first[1], last_list, random_char_list)
            print(*shown_list, '\n')
            sleep(3)
            clear()
            last_list = update_list(shown_list, first[0], first[1], 1)
            is_winner = found_winner(last_list)
            if is_winner:
                print_winner()
                return 0
        # player_2 turn
        player2_again = True
        while player2_again:
            print(*random_char_list)
            print(*last_list)
            second = get_input(input(f'Player#2-Score {score_2}: '), length, last_list)
            shown_list = show_choices(second[0], second[1], last_list, random_char_list)
            print(*shown_list, '\n')
            sleep(3)
            clear()
            last_list = update_list(shown_list, second[0], second[1], 2)
            is_winner = found_winner(last_list)
            if is_winner:
                print_winner()
                return 0


One_Line_Memory_Game()
