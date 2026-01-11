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
			import pandas as pd
			from lab6_task import preprocess as student_preprocess

			bundle = np.load('test_data.npz', allow_pickle=False)
			# numpy inputs
			X_train_np = bundle['X_train']
			X_test_np  = bundle['X_test']
			y_train_np = bundle['y_train']
			y_test_np  = bundle['y_test']

			# convert numpy inputs to pandas to match preprocess signature
			X_train = pd.DataFrame(X_train_np)
			X_test  = pd.DataFrame(X_test_np)
			y_train = pd.Series(np.asarray(y_train_np).ravel())
			y_test  = pd.Series(np.asarray(y_test_np).ravel())

			# run student's preprocess (pandas inputs)
			student_zscore = student_preprocess(X_train, X_test, y_train, y_test)

			# load reference solution and convert to pandas with matching index/columns
			sol_bundle = np.load('test1_zscore.npz', allow_pickle=False)
			sol_X_train = pd.DataFrame(sol_bundle['X_train_std'], index=X_train.index, columns=X_train.columns)
			sol_X_test  = pd.DataFrame(sol_bundle['X_test_std'],  index=X_test.index,  columns=X_test.columns)
			sol_y_train = pd.Series(np.asarray(sol_bundle['y_train_std']).ravel(), index=y_train.index)
			sol_y_test  = pd.Series(np.asarray(sol_bundle['y_test_std']).ravel(),  index=y_test.index)

			# normalize reference X using its training-set statistics so comparison is scale-invariant
			sol_train_mean = sol_X_train.mean(axis=0)
			sol_train_std  = sol_X_train.std(axis=0, ddof=0).replace(0, 1.0)

			sol_X_train_norm = (sol_X_train - sol_train_mean) / sol_train_std
			sol_X_test_norm  = (sol_X_test  - sol_train_mean) / sol_train_std

			sol_zscore_norm = (
				sol_X_train_norm,
				sol_X_test_norm,
				sol_y_train,
				sol_y_test
			)

			# compare elementwise using numpy arrays (tolerance 1e-3)
			valid = (
				isinstance(student_zscore, (list, tuple))
				and len(student_zscore) == 4
				and all(
					np.allclose(s.to_numpy(), t.to_numpy(), atol=1e-3, equal_nan=True)
					for s, t in zip(student_zscore, sol_zscore_norm)
				)
			)

			if not valid:
				# print diagnostics to help locate differences
				for i, (s, t) in enumerate(zip(student_zscore, sol_zscore_norm)):
					print(f"\n--- part {i} ---")
					print("type:", type(s), "shape:", getattr(s, "shape", None))
					# convert to numpy for numeric diffs
					s_arr = s.to_numpy() if hasattr(s, "to_numpy") else np.asarray(s)
					t_arr = t.to_numpy() if hasattr(t, "to_numpy") else np.asarray(t)
					# overall max abs diff
					diff = np.abs(s_arr - t_arr)
					print("max_abs_diff:", np.nanmax(diff))

					# if DataFrame, print per-column diagnostics
					if isinstance(s, pd.DataFrame) and isinstance(t, pd.DataFrame):
						# per-column max diff
						per_col_max = np.nanmax(np.abs(s_arr - t_arr), axis=0)
						print("per-column max_abs_diff:", per_col_max)
						# student vs solution means/stds (use training stats semantics)
						print("student col means:", s.mean(axis=0).to_numpy())
						print("sol     col means:", t.mean(axis=0).to_numpy())
						# compare std used for scaling (use ddof=0 to match typical zscore)
						print("student col std (ddof=0):", s.std(axis=0, ddof=0).to_numpy())
						print("sol     col std (ddof=0):", t.std(axis=0, ddof=0).to_numpy())
					elif isinstance(s, pd.Series) and isinstance(t, pd.Series):
						print("student mean:", s.mean(), "sol mean:", t.mean())
						print("student std (ddof=0):", s.std(ddof=0), "sol std (ddof=0):", t.std(ddof=0))
					else:
						print("values (student):", s_arr.flatten()[:10])
						print("values (sol)    :", t_arr.flatten()[:10])
		print(valid)
	except Exception as e:
		print(e)
		print()