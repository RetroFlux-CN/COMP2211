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
    print("Hidden test case 8: Test the function 'tokenize_text'")
    with HiddenPrints():
        from COMP2211_PA2 import tokenize_text

        movies_data = pd.read_csv('hidden_movies_data_preprocessed.csv')
        student_padded_sequences = tokenize_text(movies_data['cleaned_text'])

        solution = np.load("hidden_test_8_padded_sequences.npy")

    if (student_padded_sequences == solution).all():
        print(True)
    else:
        print("The output padded sequences do not match the expected output.")
        print(f"The sequences with differences (up to 5) are shown below:")
        diff_indices = np.where(student_padded_sequences != solution)[0]
        for idx in diff_indices[:5]:
            print(f"Index {idx}:")
            print(f"  Your output:     {student_padded_sequences[idx]}")
            print(f"  Expected output: {solution[idx]}")