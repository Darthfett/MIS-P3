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

from divider import get_image_cells_with_width

OUTPUT_FOLDER = os.path.join(os.path.split(__file__)[0], "../", "Outputs")

def get_dct_freq(image, image_id, color_space):
    pixels = list(image.getdata())
    width = image.size[0]

    # Split the image into 8x8 image cells
    image_cells = list(get_image_cells_with_width(pixels, width, 8, 8))

    image_cell_channels = [[[[pixel[ch] for pixel in row] for row in cell] for cell in image_cells] for ch in range(3)]

    output = []
    for channel_id, channel_cells in enumerate(image_cell_channels):
        for cell_coord, cell in enumerate(channel_cells):
            freq_components = dct2(cell)

            most_significant = freq_components[:16]
            for freq_bin, value in enumerate(most_significant):
                output.append((image_id, cell_coord, channel_id, freq_bin, value))

    return sorted(output)

def dct_freq(image, image_id, color_space):
    output = get_dct_freq(image, image_id, color_space)

    with open(os.path.join(OUTPUT_FOLDER, "Task_III_out.txt"), 'w') as f:
        f.write('\n'.join(str(s) for s in output))


def dct(channel):
    return sp_dct([float(x) for x in channel], type=2, norm='ortho')

def dct2(rows):
    dct_result = [dct(row) for row in rows]
    cols = zip(*dct_result)
    dct2_result = sum([list(dct(col)) for col in cols], [])
    return dct2_result

def dct_inverse(channel):
    return sp_idct(channel, type=2, norm='ortho')

