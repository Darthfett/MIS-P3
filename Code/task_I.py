from __future__ import division, print_function, generators

import Image as pil
import matplotlib.pyplot as plt

import itertools as it
from operator import itemgetter
import os

from pixel_converter import convert_pixel

BINS = 8
OUTPUT_FOLDER = os.path.join(os.path.split(__file__)[0], "../", "Outputs")

def split_box(box, component):
    """Given a list of colors, median-split based on the given component."""
    sorted_box = sorted(box, key=itemgetter(component))
    box1 = sorted_box[:int(len(sorted_box) / 2)]
    box2 = sorted_box[int(len(sorted_box) / 2):]
    return box1, box2

def component_range(colors, component):
    """
    Given a list of pixels, find the range of the given component.

    Component is an index, e.g. in RGB, red is 0, green is 1, blue is 2.
    """
    channels = zip(*colors)
    return max(channels[component]) - min(channels[component])

def median_cut(pixels, n):
    """Given a list of pixels, get a list of n lists, grouping the most similar pixels together."""

    # We start with one box containing all the pixels
    boxes = [pixels]

    while len(boxes) < n:
        # Split the largest box
        largest_box = max(boxes, key=len)
        ranges = [component_range(largest_box, i) for i in range(3)]

        # Get the color component with the largest range
        max_range = max(ranges)
        component_index = ranges.index(max_range)

        # Median split largest box based on the color component with largest range
        box1, box2 = split_box(largest_box, component_index)

        # Replace the largest box with the two that it split into
        i = boxes.index(largest_box)
        boxes[i:i+1] = [box1, box2]

    return boxes

def histogram(binned_pixels):
    """ Do histogram part (?). """

    # For each bin create two pixels, the first containing the smallest component values, and the second containing the largest component values for any pixel in the bin
    bin_bounds = [[tuple(min(bin, key=itemgetter(i))[i] for i in range(3)), tuple(max(bin, key=itemgetter(i))[i] for i in range(3))] for bin in binned_pixels]

    # TODO?: Normalize the bounds to include (0, 0, 0) and (255, 255, 255) even if the source does not.

    # min_ranges = [bin[0] for bin in bin_bounds]
    # max_ranges = [bin[1] for bin in bin_bounds]
    # for i in range(3):
        # min_component_i = min(min_ranges, key=itemgetter(i))
        # bin_id = min_ranges.index(min_component_i)

        # bin_bounds[bin_id][0] = bin_bounds[bin_id][0][:i] + (0, ) + bin_bounds[bin_id][0][i+1:]

        # max_component_i = max(max_ranges, key=itemgetter(i))
        # bin_id = max_ranges.index(max_component_i)

        # bin_bounds[bin_id][1] = bin_bounds[bin_id][1][:i] + (255, ) + bin_bounds[bin_id][1][i+1:]

    return bin_bounds

def get_all_the_pixels(images):
    return it.chain.from_iterable(img.getdata() for img in images)

def median_cut_histogram(images, color_space):
    # Get all the pixels
    pixels = get_all_the_pixels(images)

    # Convert to target operational color space
    pixels = [convert_pixel(pixel, "rgb", color_space) for pixel in pixels]

    binned_pixels = median_cut(pixels, BINS)

    bin_bounds = histogram(binned_pixels)

    with open(os.path.join(OUTPUT_FOLDER, "Task_I_histogram_boundaries.txt"), 'w') as out:
        out.write(str(bin_bounds))