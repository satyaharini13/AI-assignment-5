import math

def alphabeta(board, depth, alpha, beta, is_max):
    result = check_winner(board)
    scores = {'X':1,'O':-1,'draw':0}

    if result:
        return scores[result]

    if is_max:
        value = -math.inf
        for i in range(9):
            if board[i]==' ':
                board[i]='X'
                value = max(value, alphabeta(board, depth+1, alpha, beta, False))
                board[i]=' '
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
        return value
    else:
        value = math.inf
        for i in range(9):
            if board[i]==' ':
                board[i]='O'
                value = min(value, alphabeta(board, depth+1, alpha, beta, True))
                board[i]=' '
                beta = min(beta, value)
                if beta <= alpha:
                    break
        return value

def check_winner(b):
    wins=[(0,1,2),(3,4,5),(6,7,8),
          (0,3,6),(1,4,7),(2,5,8),
          (0,4,8),(2,4,6)]
    for i,j,k in wins:
        if b[i]==b[j]==b[k] and b[i]!=' ':
            return b[i]
    if ' ' not in b:
        return 'draw'
    return None

if __name__ == "__main__":
    board=[' ']*9
    print("AlphaBeta:", alphabeta(board,0,-math.inf,math.inf,True))
