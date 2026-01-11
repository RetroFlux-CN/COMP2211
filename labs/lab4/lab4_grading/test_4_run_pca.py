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
	print("Test case 4: Tests the function 'run_PCA'")
	with HiddenPrints():
		from lab4_task import run_PCA

		# create dummy dataset
		df = pd.read_pickle("standardized_activity_mix.pkl")

		solution = np.load("pca_activity_mix.npy")

		# get student's answer
		student = run_PCA(df, 5)

		# Align signs column-wise using the dot product (or correlation) with the reference
		signs = np.sign(np.nansum(student * solution, axis=0))
		signs[signs == 0] = 1  # avoid zero sign in pathological cases
		student = student * signs

	if np.allclose(student[0], solution[0], rtol=1e-7, atol=1e-8, equal_nan=True):
		print(True)
	else:
		print("run_PCA(data, n_components) does not produce the expected array.")