# logging, assertions, raise exception
import random
guess = ''
while guess not in ('heads','tails'):
    print('Guess the coin toss ! Enter h oder t:')
    guess = input()
    toss = random.randint(0,1) # o is tails, 1 is heads
    if toss == guess:
        print('You got it!')
    else:
        print('Guess again!')
        guess = input()
        if toss == guess:
            print('You got it!')
        else:
            print('You bad at this game!')
            break