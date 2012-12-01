'''
Created on Dec 1, 2012

@author: wes
'''
#Experiment with Sobel
from scipy import misc
from scipy import ndimage
import numpy
import matplotlib.pyplot as plt
import pylab as pl
from divider import get_image_cells
from PIL import Image
from numpy import ndarray




def PIL2array(img):
	'''
	converts a python image to a numpy array
	'''
    return numpy.array(img.getdata(),numpy.uint8).reshape(img.size[1], img.size[0], 3)


def get_hist_bins(img):
	'''
	given a python image, return 2 lists of 16 elements each. 1 list (bin_lowers) has the lower bounds for each bin, the other list (hist_vals)
	has the number of pixels in each bin.
	'''

	im = PIL2array(pilim)
	sx = ndimage.sobel(im, axis=0, mode = 'constant')
	sy = ndimage.sobel(im, axis=1, mode = 'constant')
	sob = numpy.hypot(sx,sy)
	hist, bin_edges = numpy.histogram(im, bins = 16)
	bin_lowers = list(numpy.array(bin_edges).reshape(-1,))
	bin_lowers.pop()
	hist_vals = list(numpy.array(hist).reshape(-1,))
	return bin_lowers, hist_vals
	



