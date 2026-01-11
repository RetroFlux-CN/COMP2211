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
	print("Test case 1: Tests the function 'encode_data'")
	with HiddenPrints():
		from lab4_task import encode_data

		# create dummy dataset
		df = pd.read_csv("activity_mix_private.csv")

		solution = pd.read_pickle("encoded_activity_mix.pkl").to_numpy()

		# get student's answer
		student = encode_data(df).to_numpy()

	if np.allclose(student, solution, rtol=1e-7, atol=1e-8, equal_nan=True):
		print(True)
	else:
		print("encode_data(df) does not produce the expected dataframe.")