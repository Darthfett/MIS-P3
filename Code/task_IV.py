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
import math





def PIL2array(img):
	'''
	converts a python image to a numpy array
	'''
	return numpy.array(img.getdata(),numpy.uint8).reshape(img.size[1], img.size[0], 3)


def get_hist_angle_bins(img):
	'''
	given a python image, return 2 lists of 16 elements each. 1 list (bin_lowers) has the lower bounds for each bin, the other list (hist_vals)
	has the number of pixels in each bin.
	'''
	
	im = PIL2array(pilim)
	sx = ndimage.sobel(im, axis=0, mode = 'constant')
	sy = ndimage.sobel(im, axis=1, mode = 'constant')
	sx = list(numpy.array(sx).reshape(-1,))
	sy = list(numpy.array(sx).reshape(-1,))
	sobel = []
	for x in sx:
		for y in sy:
			x = float(x)
			y = float(y)
			if x != 0:#Avoid a divide-by-zero error
				sobel.append(math.atan(float(y)/float(x)))
			else:
				sobel.append(math.atan(200))#what should the value be if x is 0?
	hist, bin_edges = numpy.histogram(sobel, bins = 16)
	#bin_lowers = list(numpy.array(bin_edges).reshape(-1,))#unnecessary because i've already reshaped the data?
	bin_lowers.pop()
	#hist_vals = list(numpy.array(hist).reshape(-1,))#also unnecessary?
	return bin_lowers, hist_vals
	


def angle_histogram_generator(image, image_id, color_space):
	'''
	given a pil image, the name of that image and a colorspace to work in:
	splits the image into 8x8 cells, generates a histogram for each cell.
	
	'''
	pixels = pilim.getdata()
	width = pilim.size[0]
	pixels = [convert_pixel(pixel, "rgb", color_space) for pixel in pixels]

	image_cells = list(get_image_cells(pixels, width, 8, 8))
	histogram_output = []
	for cell_coord, cell in enumerate(image_cells):
		#import pdb; pdb.set_trace()
		#print "cell_coord: ", cell_coord
		#print "cell: ", cell
		color_instance_id_list, value_list = get_hist_angle_bins(cell)
		for i in range (0,15):
			histogram_output.append((image_id, cell_coord, color_instance_id_list[i], value_list[i]))
'''
testing:
'''		
pilim = Image.open('bacon_coke.jpg')
image_id = 'bacon_coke.jpg'
color_space = "rgb"
angle_hist = angle_histogram_generator(pilim, image_id, color_space)
