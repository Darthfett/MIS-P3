"""
Task III: Implement a program which, given an image, divides it into 8x8 image cells and applies 2D-DCT
on the three color channels (in the selected color space) of each cell of the image. The program selects the 16
most significant frequency components from each of the three channels. The outputs, of the form:

(image_id, cell_coord, channel_id, freq_bin, value)

are written into a file.
"""

"""
Using scipy library to aid with dct
"""

from __future__ import division, print_function, generators
import pywt as wv
from divider import get_image_cells

def dwt_freq(cells, color_space):
    """
    do for each cell, then for each cell pick significant value and print to a file.
    output[0] is appromxiations, output[1] is details
    for output[0][n] and output[1][n], n corresponds to the cells of an image. 
    n=0 is the first cell of an image. n=N-1 is the last cell, if the image consists of N=W*H cells.
    """
    output = [[]], []]
    for cell in cells
        approx, detail = do_dwt(cell)
        output[0].append(approx)
        output[1].append(detail)
    return output

def do_dwt(cell):
    approx, detail = wv.dwt(cell, 'db1')
    return approx, detail

def undo_dwt(cA, cD):
    output = wv.idwt(cell, 'db1')
    return output