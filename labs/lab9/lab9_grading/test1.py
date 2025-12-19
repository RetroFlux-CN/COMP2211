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
	print("Public test case 1: Tests the function 'move_warriors_in_place'")
	with HiddenPrints():
		from lab9_task import move_warriors_in_place
		state = [[1, 1, 0, 0, 0, 0, 0], [0, 0], 0]
		try:
			state = move_warriors_in_place(state)
		except Exception as e:
			print("function move_warriors_in_place failed")

	if state[0] == [0, 1, 1, 0, 0, 0, 0]:
		print(True)
	else:
		print("move_warriors_in_place does not satisfy requirements.")