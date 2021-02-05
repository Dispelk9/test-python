# logging, assertions, raise exception
import random
guess = ''

def ginput():
    guess = input()
    if guess == 'h':
        guess = 1
    elif guess == 't':
        guess = 0
    return guess
while guess not in ('heads','tails'):
    print('Guess the coin toss ! Enter h oder t:')
    guess = ginput()
    toss = random.randint(0,1) # o is tails, 1 is heads
    if toss == guess:
        print('You got it!')
    else:
        print('Guess again!')
        guess = ginput()
        if toss == guess:
            print('You got it!')
        else:
            print('You bad at this game!')
            break