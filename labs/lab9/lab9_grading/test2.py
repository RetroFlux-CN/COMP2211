import sys
import os

import numpy as np

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
	print("Public test case 2: Tests the function 'evaluate'")
	with HiddenPrints():
		from lab9_task import evaluate
		state = [[1, 1, 0, 0, 0, 1, 0], [1, 0], 0]
		try:
			value = evaluate(state)
		except Exception as e:
			print("function evaluate failed")

	if value == 39:
		print(True)
	else:
		print("evaluate does not satisfy requirements.")