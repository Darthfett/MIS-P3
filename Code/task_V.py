'''
Created on Dec 1, 2012

@author: wes
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
	
	im = PIL2array(pilim)
	sx = ndimage.sobel(im, axis=0, mode = 'constant')
	sy = ndimage.sobel(im, axis=1, mode = 'constant')
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
	pixels = pilim.getdata()
	width = pilim.size[0]
	pixels = [convert_pixel(pixel, "yuv", color_space) for pixel in pixels]
	y,u,v = zip(*pixels)#pull out luminance
	import pdb; pdb.set_trace()
	image_cells = list(get_image_cells(y, width, 8, 8))
	histogram_output = []
	for cell_coord, cell in enumerate(image_cells):
		color_instance_id_list, value_list = get_hist_amp_bins(cell)
		for i in range (0,15):
			histogram_output.append((image_id, cell_coord, color_instance_id_list[i], value_list[i]))
		
pilim = Image.open('bacon_coke.jpg')
image_id = 'bacon_coke.jpg'
color_space = "rgb"
amp_hist = amplitude_histogram_generator(pilim, image_id, color_space)
 


