def show_matrix(matrix):
    for line in matrix:
        print(line)

    print("\n")


def check_matrix(matrix):

    show_matrix(matrix)

    coord = list(map(int, input("enter coords (row col): ").split()))
    number = int(input("number: "))

    while coord[0] != -1 and coord[1] != -1:
        matrix[coord[0]][coord[1]] = number

        show_matrix(matrix)

        coord = list(map(int, input("enter coords (row col): ").split()))
        number = int(input("number: "))

    return matrix
