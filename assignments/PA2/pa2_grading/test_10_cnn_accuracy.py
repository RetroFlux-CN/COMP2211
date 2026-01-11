import sys
import os

import numpy as np
import pandas as pd
import keras

class HiddenPrints:
	def __enter__(self):
		self._original_stdout = sys.stdout
		sys.stdout = open(os.devnull, 'w')

	def __exit__(self, exc_type, exc_val, exc_tb):
		sys.stdout.close()
		sys.stdout = self._original_stdout

#-#-#-#-#-#-#-#-#
#-#  TEST   #-#-#
#-#-#-#-#-#-#-#-#

if __name__ == '__main__':
	print("Public test case 10: Evaluate the accuracy of the submitted CNN model")
	with HiddenPrints():
		student_model = keras.models.load_model('cnn_model.keras')
		public_X_test = np.load('test_10_hidden_X_10_percent.npy')
		public_y_test = np.load('test_10_hidden_y_10_percent.npy')
		public_X_test = public_X_test[:int(0.1 * len(public_X_test))]
		public_y_test = public_y_test[:int(0.1 * len(public_y_test))]
		
		prediction = student_model.predict(x=public_X_test)
		predicted_classes = (prediction > 0.5).astype(int).flatten()
		accuracy = np.mean(predicted_classes == public_y_test)

	if accuracy >= 0.8:
		print(True)
	else:
		print(f"Model accuracy is {accuracy}, which is below 0.8 on a sampled public test set.")