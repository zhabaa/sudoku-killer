from killer import solve_sudoku, empty_positions
# from fillBoard import fill_board
from findnums import build_matrix
from cutimagetomany import cut_images
from checkmatrix import check_matrix

import time


def prepare_board():
    path_to_image = 'data/Screenshot_20241001_033059_Sudoku.jpg'
    path_to_images = 'data/cropped_images'

    cut_images(path_to_image, path_to_images)
    board = build_matrix(path_to_images)
    # Можно семеркам нарисовать палочки и нейронка не будет выебываться

    # board = check_matrix(board)
    
    return board


def find_solution(board):
    if solve_sudoku(board):
        solved = True
        print('solution:')

        for row in board:
            print(row)

    else:
        print('no solution')
        solved = False
    
    return solved


if __name__ == '__main__':
    print(f'Start program at {time.time()}')
    session_started = time.time()
    
    board = prepare_board()
    print(f'[+] Board preparing done {time.time() - session_started}')
    
    print(f'Starting finging solution at {time.time()}')
    finding_solution = time.time()
    
    is_solved = find_solution(board)
    
    print(f'[+] Solution found!')
    print(f'[+] Current time: {time.time() - find_solution}')
    
    print(f'[+] Result: {time.time() - session_started}')
    
    print(empty_positions)
    # if is_solved:
        