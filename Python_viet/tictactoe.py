import sys


theB = {'tL':' ','tM':' ','tR':' ','mL':' ','mM':' ','mR':' ','lL':' ','lM':' ','lR':' '}
           
def printB(board):
    print(board['tL'] + '|' + board['tM'] + '|' + board['tR'])
    print('-+-+-')
    print(board['mL'] + '|' + board['mM'] + '|' + board['mR'])
    print('-+-+-')
    print(board['lL'] + '|' + board['lM'] + '|' + board['lR'])

def check_move(move):
    while move not in [1,2,3,4,5,6,7,8,9]:
        print('Invalid try again')
        move = input()
    return move

def converter(move):
    if move == 8:
        move = 'tM'
    if move == 7:
        move = 'tL'
    if move == 9:
        move = 'tR'
    if move == 4:
        move = 'mL'
    if move == 5:
        move = 'mM'
    if move == 6:
        move = 'mR'
    if move == 1:
        move = 'lL'
    if move == 2:
        move = 'lM'
    if move == 3:
        move = 'lR'     
    return move  

def checking_con(turn, move):
    print(turn + move)

turn = 'X'
if __name__ == '__main__':
    for i in range(9):
        printB(theB)
        print(' Input move for ' + turn)
        try:
            move = input()
        except ValueError:
            print('Wrong input')
            sys.exit(1)
        move = check_move(move)
        move = converter(move)
        print(move)
        theB[move] = turn
        checking_con(turn,move)
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        print(theB)
    printB(theB)   
    