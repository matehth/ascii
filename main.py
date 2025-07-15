from PIL import Image

ASCII_CHARS_LONG = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ASCII_CHARS_SHORT = ".:-=+*#%@"
MAX_BRIGHTNESS = 255


def get_pixel_matrix(image):
    pixels = list(image.getdata())
    return [pixels[i:i + image.width] for i in range(0, len(pixels), image.width)]


def get_brightness_matrix(image, char_set):
    pixel_matrix = get_pixel_matrix(image)

    if char_set == ASCII_CHARS_SHORT:
        div = 9
    else:
        div = 3

    brightness_matrix = []
    for x in range(len(pixel_matrix)):
        col = []
        for y in range(len(pixel_matrix[x])):
            col.append(round((pixel_matrix[x][y][0] +
                              pixel_matrix[x][y][1] +
                              pixel_matrix[x][y][2]) / div))
        brightness_matrix.append(col)

    return brightness_matrix


def invert_brightness(image, char_set):
    brightness_matrix = get_brightness_matrix(image, char_set)

    if char_set == ASCII_CHARS_SHORT:
        max_brightness = 85
    else:
        max_brightness = 255

    inverted_matrix = []
    for x in range(len(brightness_matrix)):
        col = []
        for y in range(len(brightness_matrix[x])):
            col.append(abs(brightness_matrix[x][y] - max_brightness))
        inverted_matrix.append(col)

    return inverted_matrix


def get_char_matrix(image, char_set, inverted=False):
    if inverted:
        brightness_matrix = invert_brightness(image, char_set)
    else:
        brightness_matrix = get_brightness_matrix(image, char_set)

    qt = round(MAX_BRIGHTNESS / len(char_set))

    char_matrix = []
    for x in range(len(brightness_matrix)):
        col = []
        for y in range(len(brightness_matrix[x])):
            col.append(char_set[round(brightness_matrix[x][y] / qt)] * 3)
        char_matrix.append(col)

    return char_matrix


def print_ascii(image, char_set, inverted=False):
    if inverted:
        char_matrix = get_char_matrix(image, char_set, True)
    else:
        char_matrix = get_char_matrix(image, char_set)

    for x in range(len(char_matrix)):
        for y in range(len(char_matrix[x])):
            print(char_matrix[x][y], end='')
        print("")


if __name__ == "__main__":
    img = Image.open("aga.jpg")
    img.thumbnail((50, 50))

    print_ascii(img, ASCII_CHARS_SHORT)
