def print_board(board):
    for row in board:
        print("".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board,row,col,n):
    for i in range(col):
        if board[row][i]:
            return False
    
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]:
            return False

    for i,j in zip(range(row,n),range(col,-1,-1)):
        if board[i][j]:
            return False
    return True

def solve(board,col,n):
    if col>=n:
        print_board(board)
        return True

    for i in range(n):
        if is_safe(board,i,col,n):
            board[i][col]=True

            solve(board,col+1,n)
            board[i][col]=False

    return False

def solve_nq(n):
    board=[[False for _ in range(n)] for _ in range(n)]
    solve(board,0,n)

solve_nq(4)