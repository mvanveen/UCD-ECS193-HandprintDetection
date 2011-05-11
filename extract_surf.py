'''
Created on 21/04/2010

This script reads a set of image files (of the same pixels dimensions) 
from the directory defined in the PATH_ORIGIN variable . 
SURF descriptors are extracted for each of the read images. 

This script changes PATH_ORIGIN variable to the directory where your images are.

@author: jbekios
'''

import glob
#from pygame.locals import *
import cv

cv.NamedWindow("SURF", 1)

list_files = glob.glob('set1/*.jpg')
list_files.sort()

# Build a structure for storing image grayscale
im = cv.LoadImage(list_files[0], cv.CV_LOAD_IMAGE_COLOR)
imgray = cv.CreateImage(cv.GetSize(im), cv.IPL_DEPTH_8U, 1)

for file_image in list_files:
    im = cv.LoadImageM(file_image, cv.CV_LOAD_IMAGE_COLOR)
    cv.CvtColor(im, imgray, cv.CV_RGB2GRAY)
    try:
        # DRAW KEYPOINT
        print cv.ExtractSURF(imgray, None, cv.CreateMemStorage(), (0, 3000, 3, 4))[0][0][0]
    except Exception, e:
        print e
