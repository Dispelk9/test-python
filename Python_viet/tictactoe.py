import sys


theB = {'tL':' ','tM':' ','tR':' ','mL':' ','mM':' ','mR':' ','lL':' ','lM':' ','lR':' '}
    

def printB(board):
    print(board['tL'] + '|' + board['tM'] + '|' + board['tR'])
    print('-+-+-')
    print(board['mL'] + '|' + board['mM'] + '|' + board['mR'])
    print('-+-+-')
    print(board['lL'] + '|' + board['lM'] + '|' + board['lR'])

def check_move(move,zone):
    while move not in zone:
        print('Invalid try again')
        move = input()

    zone = zone.remove(move)
    
    if move == 7:
        move = 'tL'
    if move == 8:
        move = 'tM'
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

def checking_con(board,condition):
    winners = [['tL','tM','tR'],['mL','mM','mR'],['lL','lM','lR'],['tL','mL','lL'],['tM','mM','lM'],['tR','mR','lR'],['tL','mM','lR'],['tR','mM','lL']]
    for squares in winners:
        if all(board[square] == 'X' for square in squares):
            print('X won')
            condition = True
        elif all(board[square] == 'O' for square in squares):
            print('O won')
            condition = True
    return condition        

if __name__ == '__main__':
    con = False
    zone = [1,2,3,4,5,6,7,8,9]
    print('Which goes first? X or O')
    turn = 'X'
        
    for i in range(9):
        print('\n')
        printB(theB)
        print(' Input move for ' + turn + ':')
        try:
            move = input()
        except ValueError:
            print(' Wrong input ')
            sys.exit(1)
        move = check_move(move,zone)
        theB[move] = turn
        con = checking_con(theB,con)
        if con:
            print('\n Game End \n')
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    
    printB(theB)   
    
    