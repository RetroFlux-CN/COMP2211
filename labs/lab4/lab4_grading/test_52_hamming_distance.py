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
	print("Test case 5.2: Tests the function 'hamming_distance'")
	with HiddenPrints():
		from lab4_task import hamming_distance

		def test_hamming_identical_points():
			a = np.array([1, 2, 3])
			b = np.array([1, 2, 3])
			out = hamming_distance(a, b)
			return out.shape == (1,) and out[0] == 0

		def test_hamming_binary_simple():
			a = np.array([1, 0, 1, 1])
			b = np.array([0, 0, 1, 0])
			out = hamming_distance(a, b)
			return out.shape == (1,) and out[0] == 2  # positions 0 and 3 differ

		def test_hamming_strings():
			a = np.array(["A", "B", "B"])
			b = np.array(["A", "C", "B"])
			out = hamming_distance(a, b)
			return out.shape == (1,) and out[0] == 1

		def test_hamming_booleans():
			a = np.array([True, False, True])
			b = np.array([True, True, False])
			out = hamming_distance(a, b)
			return out.shape == (1,) and out[0] == 2


	if all([test_hamming_identical_points(), test_hamming_binary_simple(), test_hamming_strings(), test_hamming_booleans()]):
		print(True)
	else:
		print("hamming_distance(a, b) does not produce the expected array.")