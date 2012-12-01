"""
Task II: Implement a program which, given an image, divides it into 8-by-8 regions - called image cells. Then,
    for each cell, the program creates a 16 bin color histogram, based on the histogram specification generated in
Task I. The output of the form:

(image_id, cell_coord, color_instance_id, value)

are written into a file.
"""

from __future__ import division, print_function, generators

import matplotlib.pyplot as plt

import os
import operator as op
import itertools as it

from pixel_converter import convert_pixel
from divider import get_image_cells

OUTPUT_FOLDER = os.path.join(os.path.split(__file__)[0], "../", "Outputs")

def pixel_le(p, q):
    # perform elementwise subtraction
    sub = list(it.starmap(op.sub, zip(q, p)))

    # p is less than or equal to q iff all elements are >= 0
    if all(s >= 0 for s in sub):
        return True

    return False

def pixel_ge(p, q):
    # perform elementwise subtraction
    sub = list(it.starmap(op.sub, zip(q, p)))

    # p is greater than or equal to q iff all elements are < 0
    if all(s <= 0 for s in sub):
        return True

    return False

def bin_pixel(pixel, hist_spec):
    """Given a pixel and a histogram specification, get the index for the bin in which the pixel should be."""
    for i, bin in enumerate(hist_spec):
        if pixel_ge(pixel, bin[0]) and pixel_le(pixel, bin[1]):
            return i

    return -1

def get_histogram_spec():
    """
    Get the histogram specification output by task I.
    """
    # Get histogram specification
    with open(os.path.join(OUTPUT_FOLDER, "Task_I_histogram_boundaries.txt")) as hist_spec_file:
        hist_spec = eval(hist_spec_file.read())
    return hist_spec

def histogram_generator(image, image_id, color_space):
    """
    Given an image, target operational color space, and the histogram spec from task I,
    divide the image into 8x8 image cells, and generate a histogram for each cell,
    according to the specification generated by task I.
    """
    pixels = image.getdata()
    width = image.size[0]

    # Convert to target operational color space
    pixels = [convert_pixel(pixel, "rgb", color_space) for pixel in pixels]

    # Split the image into 8x8 image cells
    image_cells = list(get_image_cells(pixels, width, 8, 8))

    # Get histogram specification
    hist_spec = get_histogram_spec()

    histogram_output = []
    for cell_coord, cell in enumerate(image_cells):
        bin_counter = dict(zip(range(16), [0]*16))

        for pix_coord, pixel in enumerate(cell):
            # Get bin for pixel
            bin_counter[bin_pixel(pixel, hist_spec)] += 1

            # Output
        for color_instance_id, value in bin_counter.items():
            histogram_output.append((image_id, cell_coord, color_instance_id, value))

    with open(os.path.join(OUTPUT_FOLDER, "Task_II_histogram.txt"), 'w') as histogram_file:
        histogram_file.write('\n'.join(str(s) for s in histogram_output))