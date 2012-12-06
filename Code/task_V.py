
'''
To perform task V, call do_task_5(...) from below. Writes to output folder.
'''
from scipy import misc
from scipy import ndimage
import numpy
import matplotlib.pyplot as plt
import pylab as pl
from divider import get_image_cells
from PIL import Image
from numpy import ndarray
from pixel_converter import convert_pixel
import os
import pdb

OUTPUT_FOLDER = os.path.join(os.path.split(__file__)[0], "../", "Outputs")


def PIL2array(img):
    '''
    converts a python image to a numpy array
    '''
    return numpy.array(img.getdata(),numpy.uint8).reshape(img.size[1], img.size[0], 3)


def get_hist_amp_bins(img):
    '''
    given a python image, return 2 lists of 16 elements each. 1 list (bin_lowers) has the lower bounds for each bin, the other list (hist_vals)
    has the number of pixels in each bin.
    '''
    
    im = numpy.array(img)
    im = numpy.resize(im,(8,8))#reshape array to model 8x8 cell
    sx = ndimage.sobel(im, axis=0, mode = 'constant')#apply sobel operator in x-direction
    sy = ndimage.sobel(im, axis=1, mode = 'constant')#apply sobel operator in y-direction
    sob = numpy.hypot(sx,sy)
    hist, bin_edges = numpy.histogram(sob, bins = 16)#sob or im?
    bin_lowers = list(numpy.array(bin_edges).reshape(-1,))
    bin_lowers.pop()
    hist_vals = list(numpy.array(hist).reshape(-1,))
    return bin_lowers, hist_vals
    


def amplitude_histogram_generator(image, image_id, color_space):
    '''
    given a pil image, the name of that image and a colorspace to work in:
    splits the image into 8x8 cells, generates a histogram for each cell.
    
    '''
    pixels = image.getdata()
    width = image.size[0]
    pixels = [convert_pixel(pixel, color_space, "yuv") for pixel in pixels]
    c1,c2,c3 = zip(*pixels)#pull out luminance
    if color_space == "RGB" or "rgb":
        n1 = 'R'
        n2 = 'G'
        n3 = 'B'
    elif color_space == "YUV" or "yuv":
        n1 = 'Y'
        n2 = 'U'
        n3 = 'V'
    else:
        n1 = 'H'
        n2 = 'S'
        n3 = 'V'    
    histogram_output = []
    
    #for c1:
    image_cells = list(get_image_cells(c1, width, 8, 8))
    for cell_coord, cell in enumerate(image_cells):
        color_instance_id_list, value_list = get_hist_amp_bins(cell)
        for i in range (0,15):
            histogram_output.append((image_id, cell_coord, n1, color_instance_id_list[i], value_list[i]))
    #for c2:
    image_cells = list(get_image_cells(c2, width, 8, 8))
    for cell_coord, cell in enumerate(image_cells):
        color_instance_id_list, value_list = get_hist_amp_bins(cell)
        for i in range (0,15):
            histogram_output.append((image_id, cell_coord, n2, color_instance_id_list[i], value_list[i]))
    #for c3:
    image_cells = list(get_image_cells(c3, width, 8, 8))
    for cell_coord, cell in enumerate(image_cells):
        color_instance_id_list, value_list = get_hist_amp_bins(cell)
        for i in range (0,15):
            histogram_output.append((image_id, cell_coord, n3, color_instance_id_list[i], value_list[i]))
    return histogram_output
    
def do_task_5db(image,image_id, color_space, imagedb):
    output = amplitude_histogram_generator(image, image_id, color_space)
    newOutput = []
    for instance in output:
        cell_id = imagedb.get_cell_id(instance.image, instance.cell_coord)
        newOutput.append((cell_id, instance.channel_id, instance.color_instance_id, instance.value))
    imagedb.add_multiple_dct(newOutput)
    
def do_task_5(image, image_id, color_space):
    output = amplitude_histogram_generator(image, image_id, color_space)
    with open(os.path.join(OUTPUT_FOLDER, "Task_V_out.txt"), 'w') as output_file:
        output_file.write('\n'.join(str(s) for s in output))
            
'''
#testing:
pilim = Image.open('bacon_coke.jpg')
image_id = 'bacon_coke.jpg'
color_space = "rgb"
do_task_5(pilim, image_id, color_space)
'''



