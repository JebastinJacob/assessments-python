k = 1
N = int(input('enter the value of N :'))

#function to print solution
def printSolution(board):
    global k
    print(k, "-\n")
    k = k + 1
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print("\n")
    print("\n")


# function to check the soldiers can placed in the row and col
def isSafe(board, row, col):
    for i in range(col):
        if (board[row][i]):
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if (board[i][j]):
            return False;
        i -= 1
        j -= 1

    i = row
    j = col
    while j >= 0 and i < N:
        if (board[i][j]):
            return False
        i = i + 1
        j = j - 1

    return True


# recursive function to solve the problem
def solve(board, col):
    if (col == N):
        printSolution(board)
        return True

    res = False
    for i in range(N):

        if (isSafe(board, i, col)):
            board[i][col] = 1;

            res = solve(board, col + 1) or res;

            board[i][col] = 0  # backtracking algorithm

    return res


# this function solve the problem if it cannot it prints not possible
def solveNQ():
    board = [[0 for j in range(N)]
             for i in range(N)]

    if (solve(board, 0) == False):
        print("not possible")
        return
    return
solveNQ()
