import easyocr

reader = easyocr.Reader(["en"])


def find_number(i, j, path_to_images):
    result = reader.readtext(f'{path_to_images}/image{j}{i}.jpg')
    # if result:
    #   print(result[0])
    return int(result[0][1]) if result else 0


def build_matrix(path_to_images):
    matrix = [[0 for _ in range(9)] for _ in range(9)]

    for j in range(9):
        for i in range(9):
            number = find_number(i, j, path_to_images)
            matrix[j][i] = number

    return matrix
