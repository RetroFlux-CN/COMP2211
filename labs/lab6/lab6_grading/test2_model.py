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
	print("Test the architecture of MLP model (Task 2)")
	try:
		with HiddenPrints():
			from lab6_task import create_model
			import warnings
			warnings.filterwarnings('ignore', message=r'.*input_shape.*Sequential.*', category=UserWarning)

			input_dim = 32

			model = create_model(input_dim)
			model.summary()

			assert model.count_params() <= 2e4, \
				"The number of parameters of your model should be <= 20,000!"

			valid = (model.input_shape == (None, input_dim)) and (model.output_shape == (None, 1))

		print(valid)

	except Exception as e:
		print(e)
		print()