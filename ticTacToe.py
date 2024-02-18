board = [['-','-','-'], 
         ['-','-','-'],
         ['-','-','-']]

def print_board(board):
    print("\n    1 2 3")
    for i in range(3):
        print((i+1),("|"), end = " ")
        for j in range(3):
            print(board[i][j], end=' ')
        print()
    print()

print_board(board)

def check_pos(pos):
    if board[pos[0]-1][pos[1]-1] == '-':
        return True
    else:
        return False
    
def check_win(board):
    win = False
    win_var = '-'
    for i in range(3):
        if(board[i][0] == board[i][1] == board[i][2] and board[i][0] != '-'):
            win = True
            win_var = board[i][0]
            return win, win_var
    
    for j in range(3):
        if(board[0][j] == board[1][j] == board[2][j] and board[0][j] != '-'):
            win = True
            win_var = board[0][j]
            return win, win_var

    if(board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-'):
        win = True
        win_var = board[0][0]
        return win, win_var
    
    if(board[2][0] == board[1][1] == board[0][2] and board[2][0] != '-'):
        win = True
        win_var = board[2][0]
        return win, win_var
    
    return False, '-'
    
def make_pos():
    i = 0
    j = 0
    while True:
        i = int(input("Enter first: "))
        if(isinstance(i, int) and i < 4):
            break
    while True:
        j = int(input("Enter second: "))
        if(isinstance(j, int) and j < 4):
            break
    return (int(i), int(j))

flag = True
ctr = 0

global winner
winner = '-'

while flag:
    var = ''
    if ctr%2 == 1:
        var = 'o'
    else:
        var = 'x'
    print(var,"turn")
    pos = make_pos()
    if check_pos(pos):
        board[pos[0]-1][pos[1]-1] = var
        ctr += 1
    else:
        print("\nTry again!\n")
    print_board(board)
    state, winner = check_win(board)
    if state == True:
        flag = False
        print(winner, "won!")
    if state == False and ctr == 9:
        break

print("\nTie game :(")