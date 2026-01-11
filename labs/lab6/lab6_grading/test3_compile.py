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
	print("Compile model (Task 3)")

	try:
		with HiddenPrints():
			from lab6_task import create_model, compile_model
			import tensorflow as tf
			import warnings
			warnings.filterwarnings('ignore', message=r'.*input_shape.*Sequential.*', category=UserWarning)

			input_dim = 32

			model = create_model(input_dim)
			model = compile_model(model)

		# 1) Optimizer: Adam
		opt = model.optimizer.__class__.__name__
		assert opt == "Adam", \
			f"Optimizer is {opt}, expected Adam!"

		# 2) Loss: MSE
		loss_attr = model.loss
		if isinstance(loss_attr, str):
			loss_name = loss_attr
		else:
			# if it’s a function or Loss instance
			loss_name = getattr(loss_attr, "__name__", loss_attr.__class__.__name__)
		assert loss_name in ("mse", "mean_squared_error"), \
			f"Loss is {loss_name}, expected mse!"

		# DEPRECATED CHECK OF METRICS:
		# Different of tensorflow treat the package of metrics very differently
		# And student's solution of passing String / Metric Objects require different ways for checking
		# So this part is skipped.
		# # 3) Metrics: MSE & MAE.
		# user_metrics = model.compiled_metrics.metrics
		# metric_cls_names = [m.__class__.__name__ for m in user_metrics]
		# assert "MeanAbsoluteError" in metric_cls_names, \
		#     f"Metrics are {metric_cls_names}, expected MeanAbsoluteError!"
		# assert "MeanSquaredError" in metric_cls_names, \
		#     f"Metrics are {metric_cls_names}, expected MeanSquaredError!"

		# Everything's passed
		print(True)

	except Exception as e:
		print(e)
		print()