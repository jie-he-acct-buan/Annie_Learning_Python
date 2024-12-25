# import the packages
import time
import math
import random
import turtle

def dice(n):
    dice_list = []
    summ = 0
    for i in range(n):
        dice_number = random.randint(1, 6)
        dice_list.append(dice_number)
        summ = summ + dice_number
    return dice_list, summ

ask = True
while ask:
    greeting = input('Hi! Welcome to diceworld! Do you want to play a dice game with me? ').upper()
    if greeting in['YES', 'NO']:
        ask = False 
time.sleep(2)

if greeting == 'YES':
    name = input('Can you please tell me your name? ')
    time.sleep(2)
    player_win_time = 0
    dice_bot_win_time = 0
    play_time = 0

    play_again = 'YES'
    while play_again == 'YES':    
        play_time = play_time + 1
        n = int(input('How many dice do you want to roll? '))
        time.sleep(2)
        
        player = dice(n)
        dice_bot = dice(n)

        print('{} rolled{}, and the sum is {}!'.format(name, player[0], player[1]))
        time.sleep(2)
        print('Dice_bot (me) rolled {}, and the sum is {}!'.format(dice_bot[0], dice_bot[1]))
        time.sleep(2)
        
        if player[1] > dice_bot[1]:
            print('{} wins!'.format(name))
            player_win_time = player_win_time + 1
        elif player[1] == dice_bot[1]:
            print('Draw!')   
        else:
            print('Dice_bot wins!')
            dice_bot_win_time = dice_bot_win_time + 1
        time.sleep(2)
        
        ask = True
        while ask:
            play_again = input('Do you want to play again? ').upper()
            if play_again in ['YES', 'NO']:
                ask = False   

    time.sleep(2)                 
    print('We played {} rounds.'.format(play_time))
    print('{} won {} times!'.format(name, player_win_time))
    print('Dice_bot (me) won {} times!'.format(dice_bot_win_time))
    print('It was nice meeting you {}. Maybe we can play again next time. Bye!!!'.format(name))    

else:
    print('Oh darn. Maybe we can play next time. Bye!')

























