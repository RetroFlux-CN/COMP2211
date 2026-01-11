import sys
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class HiddenPrints:
	def __enter__(self):
		self._original_stdout = sys.stdout
		sys.stdout = open(os.devnull, "w")

	def __exit__(self, exc_type, exc_val, exc_tb):
		sys.stdout.close()
		sys.stdout = self._original_stdout


if __name__ == "__main__":
	print("Check if the hidden test RMSE <= 2.4")

	try:
		with HiddenPrints():
			import numpy as np
			import tensorflow as tf
			import pandas as pd
			from tensorflow import keras
			from lab6_task import preprocess, create_model
			from sklearn.metrics import mean_squared_error

			# Filter the tf warning
			import warnings
			warnings.filterwarnings('ignore', message=r'.*input_shape.*Sequential.*', category=UserWarning)

			# Explicit Pandas loading.
			# pandas.DataFrame.mean() default with column-wise vector;
			# (default) numpy.ndarray.mean() is default single scalar over ALL elements (NOT expected)
			bundle = np.load('test_data.npz', allow_pickle=False)
			X_train = pd.DataFrame(bundle['X_train'])
			X_hidden = pd.DataFrame(bundle['X_hidden'])
			y_train = pd.Series(bundle['y_train'])
			y_hidden = pd.Series(bundle['y_hidden'])

			input_dim = 32
			model_student = create_model(input_dim)
			model = keras.models.load_model('lab6_model.keras')

			# Compare meta info
			assert model_student.count_params() == model.count_params(), (
				"Parameter count mismatch between python code and keras model: "
				f"{model_student.count_params()} vs {model.count_params()}"
			)
			# Param <= 20000
			assert model.count_params() <= 20000, (
				f"Your model has {model.count_params()} params; must be ≤ 20000!"
			)

			# Performance: RMSE < 2.4
			y_mean = y_train.mean()
			y_std = y_train.std(ddof=0)
			X_train_std, X_hidden_std, y_train_std, y_hidden_std = preprocess(
				X_train, X_hidden, y_train, y_hidden
			)

			y_pred_std = model.predict(X_hidden_std, verbose=0).flatten()
			y_true = y_hidden_std * y_std + y_mean
			y_pred = y_pred_std * y_std + y_mean
			rmse = np.sqrt(mean_squared_error(y_true, y_pred))

		valid = (rmse <= 2.4)

		# print(f"RMSE = {rmse}") # Debug Only
		print(valid)

	except Exception as e:
		print(e)
		print()