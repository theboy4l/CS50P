import sys
import os
from PIL import Image, ImageOps


def main():
    input_file, output_file = validate_arguments()
    process_image(input_file, output_file)


def validate_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_ext = os.path.splitext(sys.argv[1])[1]
    output_ext = os.path.splitext(sys.argv[2])[1]
    valid_extensions = [".jpg", ".jpeg", ".png"]

    if input_ext not in valid_extensions:
        sys.exit("Invalid input")
    if output_ext not in valid_extensions:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    return sys.argv[1], sys.argv[2]


def process_image(input_path, output_path):
    try:
        user_photo = Image.open(input_path)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    shirt_size = shirt.size
    resized_photo = ImageOps.fit(user_photo, shirt_size)
    resized_photo.paste(shirt, (0, 0), shirt)
    resized_photo.save(output_path)


if __name__ == "__main__":
    main()
