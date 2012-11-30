"""
Task III: Implement a program which, given an image, divides it into 8x8 image cells and applies 2D-DCT
on the three color channels (in the selected color space) of each cell of the image. The program selects the 16
most significant frequency components from each of the three channels. The outputs, of the form:

(image_id, cell_coord, channel_id, freq_bin, value)

are written into a file.
"""

from __future__ import division, print_function, generators
import scipy as sp
from divider import get_image_cells

def dct_freq(image, color_space):
    output = do_dct(image)

def do_dct(image)
    output = sp.fftpack.dct(image, type=2)
    return output

def do_dct(image)
    output = sp.fftpack.idct(image, type=2)
    return output

def undo_dct