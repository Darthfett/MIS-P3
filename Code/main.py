from __future__ import division
from __future__ import print_function
from __future__ import generators

# 3rd party
import Image as pil

# Built-in
import os
import sys

# This package
import task_I

def get_image_files(dir):
    """Get the image filenames in directory."""
    if not os.path.isdir(dir):
        raise ValueError("Invalid directory {}".format(dir))
    extensions = {".jpg", ".png"}
    for filename in os.listdir(dir):
        if os.path.splitext(filename)[-1].lower() in extensions:
            yield os.path.join(dir, filename)

def valid_image_dir(dir_path):
    """Determine whether a directory is valid, and contains images."""
    return os.path.isdir(dir_path) and list(get_image_files(dir_path))

def get_image_dir():
    """Get a valid image directory from the user."""
    # The default image directory (../Inputs)
    default_image_dir = os.path.join(os.path.split(__file__)[0], "../", "Inputs")

    image_dir = raw_input("Enter a directory containing the images: ")
    if not image_dir:
        image_dir = default_image_dir
    while not valid_image_dir(image_dir):
        print("Invalid directory")
        image_dir = raw_input("Enter a directory containing the images: ")
    return image_dir

def get_color_space():
    """Get a valid color space from the user."""
    # The set of supported color spaces (as per instructions)
    color_spaces = {"rgb", "yuv", "hsv"}

    # The default color space
    default_color_space = "rgb"

    color_space = raw_input("Enter a target operational color space: ").lower()
    if not color_space:
        color_space = default_color_space
    while not color_space in color_spaces:
        print("Invalid color space")
        color_space = raw_input("Enter a target operational color space: ").lower()
    return color_space

def main(args):
    image_dir = get_image_dir()
    color_space = get_color_space()
    image_paths = get_image_files(image_dir)
    images = [pil.open(img) for img in image_paths]
    task_I.median_cut_histogram(images, color_space)

if __name__ == '__main__':
    main(sys.argv[1:]) # skip first argument ("main.py")