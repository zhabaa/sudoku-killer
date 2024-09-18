matrix = [
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



class SudokuKiller:
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.t_matrix = [["-" for _ in range(9)] for _ in range(9)]
        self.selected = [0, 0]

    def print_matrix(self):
        for line in self.matrix:
            print(*line)

    def transpose(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.t_matrix[i][j] = self.matrix[j][i]

    def move_selected(self):
        if self.selected[0] == 8 and self.selected[1] == 8:
            pass
        elif self.selected[0] == 8:
            self.selected[0] == 0
            self.selected[1] += 1
        else:
            self.selected[0] += 1

    def check_element(self):
        element = matrix[self.selected[1]][self.selected[0]]
        return not bool(element)

    def possible_values(self):
        if self.check_element():
            possible_values = set(list(range(1, 10)))
            
            hor = self.check_hor()
            vert = self.check_vert()
            chunk = self.check_chunk()
            
        return sorted(possible_values.difference(hor).difference(vert).difference(chunk))

    def check_hor(self):
        impossible_values = set()

        for value in self.matrix[self.selected[1]]:
            if value:
                impossible_values.add(value)

        return impossible_values

    def check_vert(self):
        impossible_values = set()

        # self.t_matrix = self.transpose()
        self.transpose()
        
        for value in self.t_matrix[self.selected[1]]:
            if value:
                impossible_values.add(value)

        return impossible_values

    def check_chunk(self):        
        chunk = []

        for j in range(3):
            if not (3 * j <= self.selected[1] < 3 * j + 3):
                continue

            for i in range(3):
                if not (3 * i <= self.selected[0] < 3 * i + 3):
                    continue

                for g in range(3 * j, 3 * j + 3):
                    chunk += self.matrix[g][3 * i : 3 * i + 3]

        return set(chunk)

    def count_free_cell(self, matrix=None):
        if matrix is not None:
            return [j for i in matrix for j in i].count(0)
        return [j for i in self.matrix for j in i].count(0)

    def move_to_zero(self):
        if not self.matrix[self.selected[0]][self.selected[1]]:
            zero = list()
            
            for index, line in enumerate(self.matrix):
                if line.find('0') == -1:
                    continue
                zero = (line.find('0'), index)
                break
        
            self.selected = zero
        
    def fill_zeros(self):
        
        matrix = self.matrix
        
        while self.count_free_cell(matrix) != 0:

            if self.matrix[self.selected[0]][self.selected[1]]:
                while self.matrix[self.selected[0]][self.selected[1]] == 0:
                    self.move_selected()
                
            posible_values = self.possible_values()
            
            if not len(posible_values):
                # откат 
                # нужно сохранить перводанную матрицу
                # если ходов больше нет то на место последнего угадывания ставить ноль
                # а если и там нет то +шаг назад
                # ...
                pass
            
            
            for number in posible_values:
                pass
                

sk = SudokuKiller(matrix)
sk.print_matrix()
print("-" * 25)
print(sk.selected)
sk.matrix[0][0] = 1
sk.print_matrix()
sk.move_to_zero() # разобраться с этой хуйней какието приколы с копией
print(sk.selected)

паудалять нахуй ненужные функции