import pyautogui as pag
import keyboard


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def change_x(self, new_x):
        self.x = new_x

    def change_y(self, new_y):
        self.y = new_y


START_FIELD = Point(1073, 182)
END_FIELD = Point(1331, 439)
START_NUM = Point(1065, 608)
END_NUM = Point(1337, 610)

solved_board = [
    [6, 1, 5, 2, 3, 7, 4, 9, 8],
    [4, 3, 2, 8, 1, 9, 7, 5, 6],
    [7, 9, 8, 6, 5, 4, 3, 1, 2],
    [2, 4, 9, 7, 6, 1, 8, 3, 5],
    [5, 6, 1, 9, 8, 3, 2, 4, 7],
    [8, 7, 3, 4, 2, 5, 1, 6, 9],
    [1, 2, 7, 5, 4, 6, 9, 8, 3],
    [9, 5, 4, 3, 7, 8, 6, 2, 1],
    [3, 8, 6, 1, 9, 2, 5, 7, 4],
]
empty_positions = {(3, 1), (3, 7), (5, 4), (4, 6), (5, 1), (5, 7), (8, 0), (0, 2), (8, 3), (0, 5), (2, 2), (1, 0), (1, 6), (0, 8), (2, 5), (8, 6), (2, 8), (6, 2), (7, 1), (7, 7), (6, 5), (4, 2), (4, 5), (3, 3), (5, 6), (4, 8), (3, 6), (5, 3), (8, 2), (8, 5), (0, 7), (2, 4), (1, 2), (0, 4), (8, 8), (2, 7), (1, 5), (6, 1), (1, 8), (7, 0), (6, 4), None, (7, 3), (3, 2), (4, 1), (4, 7), (3, 5), (4, 4), (3, 8), (5, 5), (8, 4), (0, 0), (5, 8), (8, 1), (1, 1), (0, 3), (2, 0), (8, 7), (1, 4), (2, 3), (2, 6), (7, 2), (6, 0), (6, 6), (7, 5), (7, 8)}
empty_positions.remove(None)

def get_elem(solved_board, pos):
    i, j = pos
    return solved_board[i][j]

def get_elem_coord(pos):
    x = START_FIELD.x + (pos[1] - 1) * 32 # 32 is const
    y = START_FIELD.y + (pos[0]) * 32 # 32 is const
    return x, y

def get_num_coord(num):
    x = START_NUM.x + (num - 1) * 34 # 34 is const
    y = START_NUM.y
    return x, y


def main(solved_board):
    for pos in sorted(empty_positions):
        elem = get_elem(solved_board, pos)
        elem_coord = get_elem_coord(pos)
        elem_num_coord = get_num_coord(elem)
        
        pag.doubleClick(elem_num_coord) # Выбор цифры
        pag.click(elem_coord)


if __name__ == "__main__":
    pag.PAUSE = 1.
    main(solved_board)
    # matrix = [[0 for _ in range(9)] for _ in range(9)]
    
    # for elem in empty_positions:
    #     if elem:
    #         i, j = elem
    #         matrix[i][j] = "O"
    
    # for line in matrix:
    #     print(line)