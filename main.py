from killer import solve_sudoku
from findnums import build_matrix
from cutimagetomany import cut_images

path_to_image = 'data/Screenshot_20240923_021221_Sudoku.jpg'
path_to_images = 'data/cropped_images'

cut_images(path_to_image, path_to_images)
board = build_matrix(path_to_images)

if solve_sudoku(board):
    print("solution:")
    for row in board:
        print(row)
else:
    print("no solution")
