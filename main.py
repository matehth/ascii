from PIL import Image

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_BRIGHTNESS = 255


def get_pixel_matrix(image):
    pixels = list(image.getdata())
    return [pixels[i:i + image.width] for i in range(0, len(pixels), image.width)]


def get_brightness_matrix(image):
    pixel_matrix = get_pixel_matrix(image)

    brightness_matrix = []
    for x in range(len(pixel_matrix)):
        col = []
        for y in range(len(pixel_matrix[x])):
            col.append(round((pixel_matrix[x][y][0] +
                              pixel_matrix[x][y][1] +
                              pixel_matrix[x][y][2]) / 3))
        brightness_matrix.append(col)

    return brightness_matrix


def get_char_matrix(image):
    brightness_matrix = get_brightness_matrix(image)

    qt = round(MAX_BRIGHTNESS / len(ASCII_CHARS))

    char_matrix = []
    for x in range(len(brightness_matrix)):
        col = []
        for y in range(len(brightness_matrix[x])):
            col.append(ASCII_CHARS[round(brightness_matrix[x][y] / qt)])
        char_matrix.append(col)

    return char_matrix


def print_ascii(image):
    char_matrix = get_char_matrix(image)

    for x in range(len(char_matrix)):
        for y in range(len(char_matrix[x])):
            print(char_matrix[x][y], end='')
        print("")


if __name__ == "__main__":
    car_image = Image.open("car.jpg")
    print_ascii(car_image)
