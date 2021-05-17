#Three CUP Monte

#Functions
#Function shuffle_list to shuffle the list
from random import shuffle
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list
#Function player_guess to get players guess as input by user
def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("Pick a number from 0, 1 or 2 :")
    return int(guess)
#Function check_guess to check the guess and publish the result
def check_guess(my_list,guess):
    if my_list[guess]=='O':
        print("Correct!!!")
    else:
        print("Wrong Guess!!!")
        print(my_list)
#INITIAL LIST
my_list=[' ','O',' ']
#SHUFFLE LIST
mixedup_list=shuffle_list(my_list)
#USER GUESS
guess= player_guess()
#CHECK GUESS
check_guess(mixedup_list,guess)