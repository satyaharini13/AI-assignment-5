import math

def minimax(board, depth, is_max):
    scores = {'X': 1, 'O': -1, 'draw': 0}

    result = check_winner(board)
    if result:
        return scores[result]

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = max(best, minimax(board, depth+1, False))
                board[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = min(best, minimax(board, depth+1, True))
                board[i] = ' '
        return best

def check_winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for i,j,k in wins:
        if b[i]==b[j]==b[k] and b[i] != ' ':
            return b[i]
    if ' ' not in b:
        return 'draw'
    return None

if __name__ == "__main__":
    board = [' ']*9
    print("Best score:", minimax(board, 0, True))
