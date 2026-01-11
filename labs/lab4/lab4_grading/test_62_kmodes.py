import sys
import os

import numpy as np
import pandas as pd

class HiddenPrints:
	def __enter__(self):
		self._original_stdout = sys.stdout
		sys.stdout = open(os.devnull, 'w')

	def __exit__(self, exc_type, exc_val, exc_tb):
		sys.stdout.close()
		sys.stdout = self._original_stdout

#-#-#-#-#-#-#-#
#-#  TEST   #-#
#-#-#-#-#-#-#-#

if __name__ == '__main__':
	print("Test case 6.2: Tests the function 'kmeans_clustering' with distance='hamming'")
	with HiddenPrints():
		from lab4_task import kmeans_clustering

		# create dummy dataset
		df = pd.read_pickle("standardized_activity_mix.pkl")
		data_new = df[['Program', 'Residence', 'Year']].to_numpy()

		solution = np.load("kmodes.npy")

		# get student's answer
		student = kmeans_clustering(data_new, 2, distance='hamming')

	if np.allclose(student['labels'], solution, rtol=1e-7, atol=1e-8, equal_nan=True):
		print(True)
	else:
		print("kmeans_clustering(data, clusters, max_iters, rand_state, distance='hamming') does not produce the expected array.")