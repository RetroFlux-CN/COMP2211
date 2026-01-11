import sys
import os

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

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
    print("Hidden test case 5: Test the function 'split_dataset'")
    with HiddenPrints():
        from COMP2211_PA2 import split_dataset

        # load the dummy dataset
        X = np.load("hidden_X_mlp.npy")
        movies_data = pd.read_csv('hidden_movies_data_preprocessed.csv')

        # get student's answer
        X_train_size = (6388, 5000)
        X_test_size = (1597, 5000)
        y_train_size = (6388,)
        y_test_size = (1597,)
        student = split_dataset(X, movies_data, test_split_ratio=0.2, rand_state=42)

    if (X_train_size == student[0].shape) and (X_test_size == student[1].shape) and (y_train_size == student[2].shape) and (y_test_size == student[3].shape):
        print(True)
    else:
        print("split_dataset(df, X, test_split_ratio, rand_state) does not produce the expected arrays.")
        print(f"X_train shape: {student[0].shape}, expected: {X_train_size}")
        print(f"X_test shape: {student[1].shape}, expected: {X_test_size}")
        print(f"y_train shape: {student[2].shape}, expected: {y_train_size}")
        print(f"y_test shape: {student[3].shape}, expected: {y_test_size}")