import sys
import os
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
	acc_threshold = 0.30
	print(f"Public test case 3 -> Tests if the accuracy of the model >= {acc_threshold:.2f}")
	with HiddenPrints():
		import tensorflow as tf

		print(tf.__version__)
		model = None
		rescale = tf.keras.Sequential([
			tf.keras.layers.Rescaling(1. / 255)
		])
		model = tf.keras.models.load_model('model_lab8.keras')
		testset_path = "lab8_Fall2025_test/"
		if not os.path.exists(testset_path):
			unzip_file(testset_path[:-1] + ".zip", '.')
		test_dataset = tf.keras.utils.image_dataset_from_directory(
			directory=testset_path, batch_size=25, label_mode='categorical', color_mode='grayscale',
			image_size=(64, 64), shuffle=False, class_names=['CNV', 'DME', 'DRUSEN', 'NORMAL']
		)
		test_dataset = test_dataset.map(lambda x, y: (rescale(x), y))
		val_loss, val_acc = model.evaluate(test_dataset, verbose=False)

	if val_acc >= acc_threshold:
		print(True)
	else:
		# print("Model has accuracy below 0.30 on test data")
		print(f"The model finally achieves an accuracy of {val_acc:.4f} on the test set, which falls below the required threshold of {acc_threshold:.2f}.")