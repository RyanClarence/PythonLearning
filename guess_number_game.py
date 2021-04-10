#!/usr/bin/env python3

"""
   author : Sboniso Gordon Mzizi
   guessing number game
"""
import random


def get_user_input(max_number = 5):
    user_input_value = input(f"Guess number between 1 to {max_number}  : ")
    if user_input_value.isdigit() == True:
        return int(user_input_value)
    else:
        print("Please Enter Numbers Only")
        return 0


def game_main(user_input_value):  
    number_to_guess = random.randint(1,5)
    count_chances = 3
    win_count = 0
    levels = 1
    max_number = 5

    while True:
        if user_input_value:
            if user_input_value == number_to_guess:
                print("++++++++++++++++++++++++++++++++++++++++")
                print("\nCongratulation ******** you WON\n")
                win_count += 1
                count_chances = 3
                if win_count == 4:
                    max_number *= 2
                    win_count = 0
                    levels += 1
                    print("++++++++++++++++++++++++++++++++++++++++")
                    print(f"Level {levels} Unlocked  Guess between 1 and  {max_number}")
                    print("++++++++++++++++++++++++++++++++++++++++\n")
                number_to_guess = random.randint(1,max_number)
                user_input_value = get_user_input(max_number)
                if user_input_value == 0:
                    user_input_value = get_user_input(max_number)
                    if user_input_value == 0:
                        print("YOU DONT LISTEN <> GAME OVER!")
                        break
            else:
                
                count_chances -= 1 
                if count_chances == 0:
                    print("Used Up all Chances GAME OVER!!")
                    break
                print(f"Try again {count_chances} chances left")
                user_input_value = get_user_input(max_number)
                if user_input_value == 0:
                    user_input_value = get_user_input(max_number)
                    if user_input_value == 0:
                        print("YOU DONT LISTEN <> GAME OVER!")
                        break


if __name__ =="__main__":
    print(""" 
    Welcome to GUESS NUMBER GAME, You have 3 chances to guess a number.
    this game consist of unlimited levels start from level 1
    guessing a number 4x will unlock new level.
    every time you GUESS a number, chance counter is reset to 3.
    """)
    print("\nGOOD LUCK\n")
    print("\nyou have 3 chances\n")
    user_input_value = get_user_input()
    if user_input_value != 0:
        if user_input_value >= 1 and user_input_value <= 5:
            game_main(user_input_value)
        else:
            print(f"Please enter a number between 1 and  5 ")   
    
