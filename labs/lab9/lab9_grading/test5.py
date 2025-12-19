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

#-#-#-#-#-#-#-#-
#-#  TEST   #-#-
#-#-#-#-#-#-#-#-

if __name__ == '__main__':
	print("Public test case 3: Tests the function 'minimax'")
	with HiddenPrints():
		from lab9_task import minimax
		state = [[0, 0, 0, 0, 0, 0, 0], [2, 2], 0]
		minimax.calls = 0
		try:
			best_val, best_action = minimax(state, 3)
		except Exception as e:
			print("function minimax failed")
	if best_action == "TECHNOLOGY" and best_val == 18:
		print(True)
	else:
		print("minimax does not satisfy requirements.")