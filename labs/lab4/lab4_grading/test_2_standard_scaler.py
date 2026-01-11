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
	print("Test case 2: Tests the function 'standard_scaler'")
	with HiddenPrints():
		from lab4_task import standard_scaler

		# create dummy dataset
		df = pd.read_pickle("encoded_activity_mix.pkl")

		solution_1 = pd.read_pickle("standardized_activity_mix.pkl").to_numpy()
		solution_2 = pd.read_pickle("standardized_activity_mix_2.pkl").to_numpy()

		# get student's answer
		student = standard_scaler(df)
		student = student.drop('StudentID', axis=1, errors='ignore').to_numpy()

	if np.allclose(student, solution_1, rtol=1e-7, atol=1e-8, equal_nan=True) or np.allclose(student, solution_2, rtol=1e-7, atol=1e-8, equal_nan=True):
		print(True)
	else:
		print("standard_scaler(df) does not produce the expected dataframe.")