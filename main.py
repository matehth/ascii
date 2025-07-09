from PIL import Image


def read_image(image_file):
    im = Image.open(image_file)
    return im


def get_pixel_matrix(image):
    pixels = list(image.getdata())
    return [pixels[i:i + image.width] for i in range(0, len(pixels), image.width)]


if __name__ == "__main__":

    car = read_image("car.jpg")
    print(f"Image size: {car.width} x {car.height}")

    car_pixel_matrix = get_pixel_matrix(car)
    print(car_pixel_matrix[0][0])

