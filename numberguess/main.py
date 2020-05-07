#!/usr/bin/env python3.8

import random

print('Welcome to the Guess game. You can quit any time by enterying q or ctrl + c')

def init():  
    try:
        number = int(input('enter a number between 1 and 10: '))
        return number
    except NameError:
        if(EOFError):
            print('That input is empty')
        print('Sorry, that is not a valid input')

score = 0

while True:

    number = init()

    randonnumber = random.randint(1, 10)

    if (number == randonnumber) :
        score = score + 1
        print('Hurray! Your guess is correct. ' + str(randonnumber) + ' is the correct guess')
    
        cont = input('Play again? "y" or "n" :')

        try:
            if(cont != 'y' or cont != 'n'):
                print('Enter y or n')
            if(cont == 'n'):
                break
        except NameError:
            print('Wrong input')

