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
	print("Test case 3: Tests the function 'calculate_cumulative_variance'")
	with HiddenPrints():
		from lab4_task import calculate_cumulative_variance

		# create dummy dataset
		df = pd.read_pickle("standardized_activity_mix.pkl")

		solution = np.load("cumulative_variance.npy")

		# get student's answer
		student = calculate_cumulative_variance(df)

	if np.allclose(student, solution, rtol=1e-7, atol=1e-8, equal_nan=True):
		print(True)
	else:
		print("calculate_cumulative_variance(data) does not produce the expected array.")