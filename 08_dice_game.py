#  import the packages
import random
import datetime
import time
import math
import turtle


# define the dice function
def dice(n):
    dice_list = [random.randint(1, 6) for i in range(n)]
    return dice_list


# dice game
# ask player if she/he wants to play the game
greeting = '''
Hi! welcome to diceworld! 
Do you want to play a dice game with me? 
Type "Yes" or "no"
'''
ask = True
while ask:
    play_or_not = input(greeting).upper()
    if play_or_not in ['YES', 'NO']:
        ask = False

# if the player wants to play  
if play_or_not == 'YES':
    name = input('Can you tell me your name? ')

    # if the player wants to play again 
    play_again = 'YES'
    while play_again == 'YES':
        n = int(input('How many dice do you want to roll? '))

        player = dice(n)
        dice_bot = dice(n)

        print('{} rolled {} and the sum is {}!'.format(name, player, sum(player)))
        print('Dice_bot (me) rolled {} and the sum is {}!'.format(dice_bot, sum(dice_bot)))

        if sum(player) < sum(dice_bot):
            print('Dice_bot wins!')
        elif sum(player) == sum(dice_bot):
            print('Draw!')
        else:
            print('{} wins!'.format(name))   

        # asks the player if she/he wants to play again
        ask = True
        while ask:
            play_again = input('Do you want to play again? Type "Yes" or "no" ').upper()
            if play_again in ['YES', 'NO']:
                ask = False

    # the player does not want to play again
    print('It was nice meeting you {}. Maybe we could play another time.Bye!'.format(name))


# if the player does not want to play
else:
    print('Oh darn. Maybe we can play another day. Bye!')












