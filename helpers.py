#import numpy as np

filename = 'n.txt'
data = []

def read_file(filename):
	"""reads a txt file. Format = 1 row - 1 int
	returns array with all ints"""
	data = []
	with open(filename) as f:
		for l in f.readlines():
			data.append(int(l.rstrip()))
	return data

def calculate_sum(data):
	"""arg: int-array
	return sum of integer array
	"""
	sum_ = 0
	for i in data:
		sum_ += i
	#sum_ = np.sum(data)
	return sum_
