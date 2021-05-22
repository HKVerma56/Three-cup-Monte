#!/bin/python3

import math
import os
import random
import re
import sys


# Game dctionary which contains all position and all values at position>>>>GLOBAL 
game_list={}

# Start function starts the game sets the board to default values and ask player 1 for his preferd Symbol
def start():
    print('Lets Start Tic-Tac-Toe')
    global game_list
    game_list={1:'#',2:'#',3:'#',4:'#',5:'#',6:'#',7:'#',8:'#',9:'#'}
    global p1
    global p2
    p1='H'
    while p1 not in ['X','O']:
        p1=input("Player 1: Choose X or O >>>").upper()
        if p1=="X":
            p2='O'
        elif p1=='O':
            p2="X"
        else:
            p1='H'
    print('Player1 Start')

#display function shows the game board and positions info
def display():
    print('\n \n\n \n')
    print("::::::::::::::GAME BOARD::::::::::::::")
    print("   |   |   ")
    print(f" {game_list[1]} | {game_list[2]} | {game_list[3]} ")
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(f" {game_list[4]} | {game_list[5]} | {game_list[6]} ")
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(f" {game_list[7]} | {game_list[8]} | {game_list[9]} ")
    print("   |   |   ")
    print('\n \n')
    print("::::::::::::::Positions::::::::::::::")
    print("   |   |   ")
    print(" 1 | 2 | 3 ")
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(" 4 | 5 | 6 ")
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(" 7 | 8 | 9 ")
    print("   |   |   ")
    print('\n \n')


# choice function asks for position where player wants to place the value and checks if the value is correct or not and also validates weather the place is available or not
def choice():
    pos="ppw"
    while pos not in range(0,10):
        pot= input("Enter The Position:")
        if pot.isdigit():
            pos=int(pot)
        else:
            pos="ppw"
        if pos in range(0,10) and game_list[(pos)] =="#":
            return (pos)
        else:
            pos="ppw"
    
# rep function takes position and sign and put the sign at desired position
def rep(pos,pn):
    game_list[pos]=pn


# check function checks all the condition and retuns values to determine weather gaame shood proceed or not and also if some one won who is the winner
def check(pn):
    global game_status
    global winner
    if pn==p1:
        player="Player 1"
    else:
        player='Player 2'
    winner="None"
    if game_list[1]== game_list[2] and game_list[2]==game_list[3] and game_list[2]!='#':
        game_status=1
        winner=player
    elif game_list[4]== game_list[5] and game_list[5]==game_list[6] and game_list[6]!='#':
        game_status=1
        winner=player
    elif  game_list[7]== game_list[8] and game_list[8]==game_list[9] and game_list[9]!='#':
        game_status=1
        winner=player
    elif  game_list[1]== game_list[4] and game_list[4]==game_list[7] and game_list[7]!='#':
        game_status=1
        winner=player
    elif  game_list[2]== game_list[5] and game_list[5]==game_list[8] and game_list[5]!='#':
        game_status=1
        winner=player
    elif  game_list[3]== game_list[6] and game_list[3]==game_list[9] and game_list[6]!='#':
        game_status=1
        winner=player
    elif  game_list[1]== game_list[5] and game_list[5]==game_list[9] and game_list[1]!='#':
        game_status=1
        winner=player
    elif  game_list[3]== game_list[5] and game_list[7]==game_list[3] and game_list[5]!='#':
        game_status=1
        winner=player
    else:
        winner='none'
    
#what function asks player if he wants to play again
def what():
    global game_start
    ren=0
    while ren==0:
        st=input('Do you want to play again: YES or NO>>>').upper()
        if st=='YES':
            game_start=0
            ren=1
        elif st=='NO':
            game_start=1
            ren=1
        else:
            ren=0
    

#Main part of code 
game_start=0
while game_start==0:
    start()
    game_status=0
    while game_status==0:
        display()
        for i in [p1,p2]:
            pn=i
            if pn==p1:
                pi=1
            else:
                pi=2
            print(f"Player{pi} turn >> fill {pn}:")
            pos=choice()
            rep(pos,pn)
            check(pn)
            display()
            has=list(game_list.values())
            if game_status==0 and ('#' not in has):
                print("Game Draw") 
                game_status=2
                break   
            elif game_status==1:
                print(winner+" is the Winner.")
                break
            else:
                pass
    what()
    
                
        
print('Thanks For Playing!!!') 
