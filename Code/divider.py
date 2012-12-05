from __future__ import division, generators, print_function

from math import ceil

def get_image_cells(pixels, width, sq_width, sq_height):
    """
    Given a list of the pixels of an image, and the image width,
    generate a list of all image cells containing sq_width x sq_height pixels.

    For images with a width that is not a multiple of sq_width, or a height that is not a multiple of sq_height,
    the last row and/or column of pixels will simply be cut off, containing a smaller number of pixels than sq_width * sq_height.
    """

    height = int(ceil(len(pixels) / width))

    new_height = int(ceil(height / sq_height))
    new_width = int(ceil(width / sq_width))
    for top in range(0, new_height*sq_height, sq_height):
        for left in range(0, new_width*sq_width, sq_width):

            if (top == (new_height*sq_height)-sq_height):
                sh = height-top
            else:
                sh = sq_height

            if (left == (new_width*sq_width)-sq_width):
                sw = width-left
            else:
                sw = sq_width

            rows = []
            for i in range(sh):
                rows.extend(pixels[((top + i) * width) + left : ((top + i) * width) + (left + sw)])
            yield rows

def get_image_cells_with_width(pixels, width, sq_width, sq_height):
    """
    Given a list of the pixels of an image, and the image width,
    generate a list of all image cells containing sq_width x sq_height pixels.

    For images with a width that is not a multiple of sq_width, or a height that is not a multiple of sq_height,
    the last row and/or column of pixels will simply be cut off, containing a smaller number of pixels than sq_width * sq_height.
    """

    height = int(ceil(len(pixels) / width))

    new_height = int(ceil(height / sq_height))
    new_width = int(ceil(width / sq_width))
    for top in range(0, new_height*sq_height, sq_height):
        for left in range(0, new_width*sq_width, sq_width):

            if (top == (new_height*sq_height)-sq_height):
                sh = height-top
            else:
                sh = sq_height

            if (left == (new_width*sq_width)-sq_width):
                sw = width-left
            else:
                sw = sq_width

            rows = []
            for i in range(sh):
                rows.append(pixels[((top + i) * width) + left : ((top + i) * width) + (left + sw)])
            yield rows