def is_safe(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True


def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


board = [
    [0, 8, 0, 0, 0, 0, 6, 0, 0],
    [0, 7, 0, 1, 0, 3, 0, 9, 2],
    [9, 2, 1, 0, 8, 0, 0, 0, 7],
    [0, 0, 0, 6, 3, 8, 0, 0, 0],
    [0, 6, 8, 4, 5, 9, 7, 2, 0],
    [5, 0, 3, 0, 0, 7, 9, 8, 0],
    [0, 0, 0, 0, 0, 0, 1, 7, 8],
    [8, 5, 7, 0, 0, 0, 0, 0, 0],
    [2, 1, 9, 0, 0, 4, 3, 0, 0],
]

if solve_sudoku(board):
    print("Решение найдено:")
    for row in board:
        print(row)
else:
    print("Решение не существует.")
