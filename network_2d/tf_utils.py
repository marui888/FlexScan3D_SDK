# encoding:utf-8
import numpy as np

import cv2
from PIL import Image

import time
import os
import copy
import config as cfg

def input_data(classtype, rootpath_label=cfg.TESTLABEL_PATH, rootpath_image=cfg.TEST_PATH):
	new = 1
	image = []
	label = []
	dir_ = []
	if new:
		childlist_image = os.listdir(rootpath_image)
		childlist_image.sort()

		for child_dir in childlist_image:
			#print (child_dir)
			childpath_image = os.path.join('%s/%s' % (rootpath_image, child_dir))
			childpath_label = os.path.join('%s/%s' % (rootpath_label, child_dir))
				#secchildpath_image = secchildpath_image[0:-3] + 'jpg'
			image+=[childpath_image]
			label+=[childpath_label]
			dir_+=[child_dir]

	print('Find ', len(image), ' images')
	return image, label, dir_
