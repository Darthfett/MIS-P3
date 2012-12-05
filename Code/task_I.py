"""
Task I: Implement a program which divides the selected color space into 16 bins based on the color pixels
in all the image files in the data set using the median-cut algorithm. The resulting histogram specification
(consisting of color instance boundaries) is written into a file.
"""

from __future__ import division, print_function, generators

import Image as pil
import matplotlib.pyplot as plt

import itertools as it
from operator import itemgetter
import os

from pixel_converter import convert_pixel

BINS = 16
OUTPUT_FOLDER = os.path.join(os.path.split(__file__)[0], "../", "Outputs")

class Bin(object):
    """A bin object contains pixel values, and a range of pixel values covered by the bin."""
    attrs = {'pixels', 'mins', 'maxes'}

    def __str__(self):
        return str([self.mins, self.maxes])

    def __len__(self):
        return len(self.pixels)

    __repr__ = __str__

    def __init__(self, pixels=None, mins=(0, 0, 0), maxes=(255, 255, 255)):

        if hasattr(pixels, '__dict__') and Bin.attrs.issubset(set(pixels.__dict__.keys())):
            # Copy constructor
            self.pixels = list(pixels.pixels)
            self.mins = pixels.mins
            self.maxes = pixels.maxes
        else:
            if pixels is None:
                self.pixels = []
            else:
                self.pixels = pixels

            self.mins = mins
            self.maxes = maxes

def get_median(pixels, component):
    """Given a list of pixels and a component, find the median value."""
    left = int(len(pixels) / 2)
    if len(pixels) % 2 == 0:
        return sorted(pixels, key=itemgetter(component))[left][component]
    else:
        return sum(pixel[component] for pixel in sorted(pixels, key=itemgetter(component))[left:left + 1]) / 2

def split_box(box, component):
    """Given a list of colors, median-split based on the given component."""
    sorted_box = sorted(box, key=itemgetter(component))
    box1 = sorted_box[int(len(sorted_box) / 2):]
    box2 = sorted_box[:int(len(sorted_box) / 2)]
    return box1, box2

def split_bin(bin, component):
    """Given a bin and a component, median split the bin on the given component."""
    mid = get_median(bin.pixels, component)

    new_bin = Bin(bin)

    bin.pixels, new_bin.pixels = split_box(bin.pixels, component)

    bin.mins = bin.mins[:component] + (mid, ) + bin.mins[component+1:]
    new_bin.maxes = new_bin.maxes[:component] + (mid, ) + new_bin.maxes[component+1:]

    if any(bin.mins[i] > bin.maxes[i] for i in range(3)):
        import pdb; pdb.set_trace()

    if any(new_bin.mins[i] > new_bin.maxes[i] for i in range(3)):
        import pdb; pdb.set_trace()

    return bin, new_bin


def component_range(bin, component):
    """
    Given a bin, find the range of values for the given component.

    Component is an index, e.g. in RGB, red is 0, green is 1, blue is 2.
    """
    colors = bin.pixels
    channels = zip(*colors)
    return max(channels[component]) - min(channels[component])

def median_cut(pixels, n):
    """Given a list of pixels, get a list of n bins, grouping the most similar pixels together."""

    # We start with one box containing all the pixels
    bins = [Bin(pixels)]

    while len(bins) < n:
        # Split the largest box
        largest_box = max(bins, key=len)
        ranges = [component_range(largest_box, i) for i in range(3)]

        # Get the color component with the largest range
        max_range = max(ranges)
        component_index = ranges.index(max_range)

        # Median split largest box based on the color component with largest range
        box1, box2 = split_bin(largest_box, component_index)

        # Replace the largest box with the two that it split into
        i = bins.index(largest_box)
        bins[i:i+1] = [box1, box2]

    return bins

def get_all_the_pixels(images):
    return it.chain.from_iterable(img.getdata() for img in images)

def get_histogram_spec(images, color_space):
    # Get all the pixels
    pixels = get_all_the_pixels(images)

    # Convert to target operational color space
    pixels = [convert_pixel(pixel, "rgb", color_space) for pixel in pixels]

    bins = median_cut(pixels, BINS)

    return bins


def median_cut_histogram(images, color_space):
    bins = get_histogram_spec(images, color_space)

    with open(os.path.join(OUTPUT_FOLDER, "Task_I_histogram_boundaries.txt"), 'w') as out:
        out.write(str(bins))