#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import os

from optparse import OptionParser

if __name__ == '__main__':

	# Parse options command line
	parser = OptionParser()
	parser.add_option("-f", "--filename", dest="filename", metavar="FILE")

	# Process options and args
	(options, args) = parser.parse_args()
	if options.filename is None:
		parser.error("required -f [filename] arg.")

	data = np.zeros(shape=(30,8))
	lines = open(options.filename, 'r').readlines()
	for line in lines:
		vertex, sensors = line.strip().split(',')
		for sensor in sensors.split('_'):
			data[vertex, int(sensor) - 1] = 1
