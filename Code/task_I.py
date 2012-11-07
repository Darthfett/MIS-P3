
import Image as pil

import itertools as it
from pixel_converter import convert_pixel

def median_cut(pixels):
    """Given a list of pixels, perform median cut algorithm on them."""
    pass

def histogram():
    """ Do histogram part (?). """
    BINS = 16

def get_all_the_pixels(images):
    return it.chain.from_iterable(img.get_data() for img in images)

def median_cut_histogram(images, color_space):
    # Get all the pixels
    pixels = get_all_the_pixels(images)

    # Convert to target operational color space
    pixels = [convert_pixel(pixel, "RGB", color_space) for pixel in pixels]