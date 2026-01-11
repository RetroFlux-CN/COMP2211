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
	print("Calculate Z_score (Task 1)")

	try:
		with HiddenPrints():
			import numpy as np
			from lab6_task import preprocess

			bundle = np.load('test_data.npz', allow_pickle=False)
			X_train = bundle['X_train']
			X_test = bundle['X_test']
			y_train = bundle['y_train']
			y_test = bundle['y_test']

			student_zscore = preprocess(X_train, X_test, y_train, y_test)

			sol_bundle = np.load('test1_zscore.npz', allow_pickle=False)
			sol_zscore = (
				sol_bundle['X_train_std'],
				sol_bundle['X_test_std'],
				sol_bundle['y_train_std'],
				sol_bundle['y_test_std']
			)

			valid = (len(student_zscore) == len(sol_zscore)
						and all(np.allclose(s, t, atol=1e-3) for s, t in zip(student_zscore, sol_zscore)))

		print(valid)

	except Exception as e:
		print(e)
		print()