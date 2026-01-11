import sys
import os

import numpy as np
import pandas as pd

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
    print("Hidden test case 4: Test the function 'tfidf_vectorization'")
    with HiddenPrints():
        from COMP2211_PA2 import tfidf_vectorization

        df = pd.read_csv("hidden_movies_data_preprocessed.csv")[0:5]
        solution = np.load('hidden_test_4_X.npy')

        student = tfidf_vectorization(df['preprocessed_text_mlp'], 5000)

    if (solution == student).all():
        print(True)
    else:
        print("tfidf_vectorization(df, max_features) does not produce the expected array.")
        print(f"The first 5 rows with differences are shown below:")
        diff = np.where(solution != student)
        for i in range(min(5, len(diff[0]))):
            r, c = diff[0][i], diff[1][i]
            print(f"Row {r}, Column {c}: expected {solution[r, c]}, but got {student[r, c]}")