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

#-#-#-#-#-#-#-#-
#-#  TEST   #-#-
#-#-#-#-#-#-#-#-

if __name__ == '__main__':
	print("Public test case 2 -> Tests the function `train_test_split`")
	with HiddenPrints():
		from lab8_task import train_test_split
		import inspect
		import tensorflow as tf
		score = 0
		trainset_path = 'lab8_Fall2025_train/'
		if not os.path.exists(trainset_path):
			unzip_file(trainset_path[:-1] + ".zip", '.')

		full_dataset = tf.keras.utils.image_dataset_from_directory(
				directory=trainset_path, label_mode='categorical', color_mode='grayscale',
				image_size=(64, 64), batch_size=25, class_names=['CNV', 'DME', 'DRUSEN', 'NORMAL']
		)
		source = inspect.getsource(train_test_split)
		if "left_size=32" in source.replace(" ", ""):
			score += 1

	if (score == 1):
		print(True)
	else:
		print("train_test_split does not satisfy requirements.")