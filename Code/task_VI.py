"""
Task III: Implement a program which, given an image, divides it into 8x8 image cells and applies 2D-DCT
on the three color channels (in the selected color space) of each cell of the image. The program selects the 16
most significant frequency components from each of the three channels. The outputs, of the form:

(image_id, cell_coord, channel_id, freq_bin, value)

are written into a file.
"""

from __future__ import division, print_function, generators

import pywt

import os
from itertools import izip_longest

from divider import get_image_cells

def grouper(n, iterable, fillvalue=None): # this is an itertools recipe function
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

OUTPUT_FOLDER = os.path.join(os.path.split(__file__)[0], "../", "Outputs")
def dwt_freq_generator(image, image_id, color_space):
    pixels = list(image.getdata())
    width = image.size[0]

    # Split the image into 8x8 image cells
    image_cells = list(get_image_cells(pixels, width, 8, 8))

    output = []
    for cell_coord, cell in enumerate(image_cells):
        channels = zip(*cell)

        for channel_id, channel in enumerate(channels):
            freq_components = sum([list(x) for x in dwt(list(grouper(width, channel)))], [])

            most_significant = freq_components[:16]
            for freq_bin, value in enumerate(most_significant):
                output.append((image_id, cell_coord, channel_id, freq_bin, value))
    return output
def dwt_freqdb(image, image_id, color_space, imagedb):
    output = dwt_freq_generator(image, image_id, color_space)
    newOutput = []
    for (image_id, cell_coord, channel_id, freq_bin, value) in output:
        cell_id = imagedb.get_cell_id(image_id, cell_coord)
        newOutput.append((cell_id, channel_id, freq_bin, float(value)))
    imagedb.add_multiple_dwt(newOutput)
    
def dwt_freq(image, image_id, color_space):
    output = dwt_freq_generator(image, image_id, color_space)
    with open(os.path.join(OUTPUT_FOLDER, "Task_VI_out.txt"), 'w') as output_file:
        output_file.write('\n'.join(str(s) for s in output))


def dwt(channel):
    cA, (cH,cV,cD) = pywt.dwt2(channel, 'db1')
    return list(cD)

