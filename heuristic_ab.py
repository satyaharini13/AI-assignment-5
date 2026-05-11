import math

def heuristic(board):
    return board.count('X') - board.count('O')

def alphabeta(board, depth, alpha, beta, is_max, max_depth=3):
    if depth == max_depth:
        return heuristic(board)

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

if __name__ == "__main__":
    board=[' ']*9
    print("Heuristic AB:", alphabeta(board,0,-math.inf,math.inf,True))
