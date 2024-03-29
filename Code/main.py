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
import image_retrieval as ir

#Task VII
def batch_option():
    response = raw_input("Would you like to perform a batch process?  y/n: ").lower()
    return response

def process_batch(dir):
    image_paths = ir.get_image_files(dir)
    images = [pil.open(img) for img in image_paths]
    image_paths_str = ir.get_batch_images(dir)
    
    db = ir.get_database_name()
    imagedb = imagedata.myDB(db)
    imagedb.make_db()
    color_space = ir.get_color_space()
    print("=========== Batch Processing ===========")
    print("================ Task I ================")
    task_I.median_cut_histogram(images, color_space)    
    for index, image in enumerate(images):        
        #perform tasks 2 - 6
        image_id = image_paths_str[index]
        print("================ Task II ================")
        task_II.histogram_gendb(image, image_id, color_space, imagedb)
        print("================ Task III ================")
        task_III.dct_freqdb(image, image_id, color_space, imagedb)
        
        print("================ Task IV ================")
        task_IV.do_task_4db(image, image_id, color_space, imagedb)
        print("================ Task V ================")
        task_V.do_task_5db(image, image_id, color_space, imagedb)
        print("================ Task VI ================")
        task_VI.dwt_freqdb(image, image_id, color_space, imagedb)

def main(args):
    image_dir = ir.get_image_dir()
    color_space = ir.get_color_space()
    image_paths = ir.get_image_files(image_dir)
    images = [pil.open(img) for img in image_paths]

    print("================ Task I ================")
    task_I.median_cut_histogram(images, color_space)

    print("================ Task II ================")
    image, image_id = ir.get_image()
    task_II.histogram_generator(image, image_id, color_space)

    print("================ Task III ================")
    image, image_id = ir.get_image()
    task_III.dct_freq(image, image_id, color_space)

    print("================ Task IV ================")
    image, image_id = ir.get_image()
    task_IV.do_task_4(image, image_id, color_space)

    print("================ Task V ================")
    image, image_id = ir.get_image()
    task_V.do_task_5(image, image_id, color_space)

    print("================ Task VI ================")
    image, image_id = ir.get_image()
    task_VI.dwt_freq(image, image_id, color_space)

    print("================ Task VII ================")
    response = batch_option()
    if response == 'y':
        batch_dir = ir.get_image_dir()
        process_batch(batch_dir)

if __name__ == '__main__':
    main(sys.argv[1:]) # skip first argument ("main.py")
