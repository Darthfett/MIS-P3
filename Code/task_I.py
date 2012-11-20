
import Image as pil

import itertools as it
from operator import itemgetter

from pixel_converter import convert_pixel

def split_box(box, component):
    """Given a list of colors, median-split based on the given component."""
    sorted_box = sorted(box, key=itemgetter(component))
    box1 = sorted_box[:(len(sorted_box)/2)]
    box2 = sorted_box[(len(sorted_box)/2):]
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

def histogram():
    """ Do histogram part (?). """
    BINS = 16

def get_all_the_pixels(images):
    return it.chain.from_iterable(img.getdata() for img in images)

def median_cut_histogram(images, color_space):
    # Get all the pixels
    pixels = get_all_the_pixels(images)

    # Convert to target operational color space
    pixels = [convert_pixel(pixel, "rgb", color_space) for pixel in pixels]