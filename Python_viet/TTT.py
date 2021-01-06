

theB = {'tL':' ','tM':' ','tR':' ','mL':' ','mM':' ','mR':' ','lL':' ','lM':' ','lR':' '}

def printB(board):
        print(board['tL'] + '|' + board['tM'] + '|' + board['tR'])
        print('-+-+-')
        print(board['mL'] + '|' + board['mM'] + '|' + board['mR'])
        print('-+-+-')
        print(board['lL'] + '|' + board['lM'] + '|' + board['lR'])
turn = 'X'
for i in range(9):
    printB(theB)
    print(' Input move for ' + turn)
    move = input()
    theB[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printB(theB)        