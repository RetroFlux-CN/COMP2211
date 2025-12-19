import sys
import os
import numpy as np
from utils import unzip_file

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
	print("Public test case 1 -> Tests the function `load_dataset`")
	with HiddenPrints():
		from lab8_task import load_dataset
		import inspect
		import tensorflow as tf
		score = 0
		trainset_path = 'lab8_Fall2025_train/'
		if not os.path.exists(trainset_path):
			unzip_file(trainset_path[:-1] + ".zip", '.')
		try:
			ds = load_dataset(trainset_path)
		except Exception as e:
			print("Running function failed")
		source = inspect.getsource(load_dataset)
		if "label_mode='categorical'" in source.replace(" ", ""):
			score += 1
		if "color_mode='grayscale'"  in source.replace(" ", ""):
			score += 1
		if "batch_size=25," in source.replace(" ", ""):
			score += 1
		if "image_size=(64,64)" in source.replace(" ", "").replace(" ", ""):
			score += 1

	if (score==4):
		print(True)
	else:
		print("load_dataset does not satisfy requirements.")