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
	print("Public test case 5: Tests the function 'alphabeta' for its pruning")
	with HiddenPrints():
		from lab9_task import alphabeta
		state = [[0, 0, 0, 0, 0, 0, 0], [2, 2], 0]
		alphabeta.calls = 0
		try:
			best_val, best_action = alphabeta(state, 3, -999999, 999999)
		except Exception as e:
			print("function alphabeta failed")
	if best_action == "TECHNOLOGY" and best_val == 18 and alphabeta.calls == 12:
		print(True)
	else:
		print("alphabeta does not satisfy requirements.")