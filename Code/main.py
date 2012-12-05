from __future__ import division, print_function, generators

# 3rd party
import Image as pil

# Built-in
import os
import sys
from datetime import datetime

# This package
import task_I
import task_II
import task_III
import task_IV
import task_V
import task_VI
import imagedata

def get_image_files(dir):
    """Get the image filenames in directory."""
    if not os.path.isdir(dir):
        raise ValueError("Invalid directory {}".format(dir))
    extensions = {".jpg", ".png", ".bmp"}
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

def get_image():
    image_fn = ''
    while not image_fn:
        image_fn = raw_input("Enter the path to an image: ")

        if not os.path.isfile(image_fn):
            image_fn = ''

    return pil.open(image_fn), os.path.split(image_fn)[1]

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

def get_database_name():
    # The default color space
    default_database = "test"+str(datetime.today().minute)+".db"

    filename = raw_input("Enter a database filename: ").lower()
    db = filename+str(datetime.today().minute)

    if not db:
        db = default_database

    return db

def main(args):
    image_dir = get_image_dir()
    color_space = get_color_space()
    image_paths = get_image_files(image_dir)
    images = [pil.open(img) for img in image_paths]

    # DB stuff
    db = get_database_name()
    imagedb = imagedata.myDB(db)
    imagedb.make_db()

    print("================ Task I ================")
    task_I.median_cut_histogram(images, color_space)

    print("================ Task II ================")
    image, image_id = get_image()
    task_II.histogram_generator(image, image_id, color_space)
    # task_II.histogram_generator(image, image_id, color_space, imagedb)
    # print("\a")#system beep
    print("================ Task III ================")
    image, image_id = get_image()
    task_III.dct_freq(image, image_id, color_space)
    # task_III.dct_freq(image, image_id, color_space, imagedb)
    # print("\a")#system beep
    print("================ Task IV ================")
    image, image_id = get_image()
    task_IV.do_task_4(image, image_id, color_space)
    # task_IV.do_task_4(image, image_id, color_space, imagedb)

    print("================ Task V ================")
    image, image_id = get_image()
    task_V.do_task_5(image, image_id, color_space)
    # task_V.do_task_5(image, image_id, color_space, imagedb)

    print("================ Task VI ================")
    image, image_id = get_image()
    task_VI.dwt_freq(image, image_id, color_space)
    # task_VI.dwt_freq(image, image_id, color_space, imagedb)

if __name__ == '__main__':
    main(sys.argv[1:]) # skip first argument ("main.py")