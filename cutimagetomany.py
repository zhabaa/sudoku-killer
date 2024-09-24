from PIL import Image

start = (39, 431)
cell_border = 3
chunk_border = 6
cell_size = 107


def cut_images(path_to_image, path_to_images):
    img = Image.open(path_to_image)

    selecter = [start[0], start[1]]

    for j in range(9):
        for i in range(9):
            img.crop(
                (
                    selecter[0],
                    selecter[1],
                    selecter[0] + cell_size,
                    selecter[1] + cell_size,
                )
            ).save(f'{path_to_images}/{"image" + str(j) + str(i)}.jpg')
            
            # TODO: easyocr принимает np.arrays так что можно не сохранять изображения
            # сделать вывод цифры для проверки (мб)

            selecter[0] += 107

            if i == 2 or i == 5:
                selecter[0] += chunk_border
            else:
                selecter[0] += cell_border

        selecter[1] += 107
        selecter[0] = start[0]

        if j == 2 or j == 5:
            selecter[1] += chunk_border
        else:
            selecter[1] += cell_border

