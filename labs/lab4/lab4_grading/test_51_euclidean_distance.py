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
	print("Test case 5.1: Tests the function 'euclidean_distance'")
	with HiddenPrints():
		from lab4_task import euclidean_distance

		def test_euclidean_identical_points():
			a = np.array([1.0, 2.0, 3.0])
			b = np.array([1.0, 2.0, 3.0])
			out = euclidean_distance(a, b)
			return out.shape == (1,) and np.isclose(out[0], 0.0)


		def test_euclidean_simple_2d():
			a = np.array([0.0, 0.0])
			b = np.array([3.0, 4.0])
			out = euclidean_distance(a, b)
			return out.shape == (1,) and np.isclose(out[0], 5.0)


		def test_euclidean_negative_coords():
			a = np.array([-1.0, -2.0])
			b = np.array([3.0, 2.0])
			out = euclidean_distance(a, b)
			return out.shape == (1,) and np.isclose(out[0], np.sqrt(32.0))


	if all([test_euclidean_identical_points(), test_euclidean_simple_2d(), test_euclidean_negative_coords()]):
		print(True)
	else:
		print("euclidean_distance(a, b) does not produce the expected array.")