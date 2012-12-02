"""
Task III: Implement a program which, given an image, divides it into 8x8 image cells and applies 2D-DCT
on the three color channels (in the selected color space) of each cell of the image. The program selects the 16
most significant frequency components from each of the three channels. The outputs, of the form:

(image_id, cell_coord, channel_id, freq_bin, value)

are written into a file.
"""

from __future__ import division, print_function, generators

from scipy.fftpack import dct as sp_dct, idct as sp_idct

import os

from divider import get_image_cells

OUTPUT_FOLDER = os.path.join(os.path.split(__file__)[0], "../", "Outputs")

def dct_freq(image, image_id, color_space):
    pixels = list(image.getdata())
    width = image.size[0]

    # Split the image into 8x8 image cells
    image_cells = list(get_image_cells(pixels, width, 8, 8))

    output = []
    for cell_coord, cell in enumerate(image_cells):
        channels = zip(*cell)

        for channel_id, channel in enumerate(channels):
            freq_components = dct(channel)

            most_significant = freq_components[:16]
            for freq_bin, value in enumerate(most_significant):
                output.append((image_id, cell_coord, channel_id, freq_bin, value))

    with open(os.path.join(OUTPUT_FOLDER, "Task_III_out.txt"), 'w') as f:
        f.write('\n'.join(str(s) for s in output))


def dct(channel):
    return sp_dct([float(x) for x in channel], type=2, norm='ortho')

def dct_inverse(channel):
    return sp_idct(channel, type=2, norm='ortho')

