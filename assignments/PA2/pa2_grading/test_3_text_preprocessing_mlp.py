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
    print("Hidden test case 3: Test the function 'text_preprocessing_mlp'")
    with HiddenPrints():
        from COMP2211_PA2 import text_preprocessing_mlp

        df = pd.read_csv('hidden_movies_data_preprocessed.csv').iloc[:20]
        
        student = df.cleaned_text.apply(text_preprocessing_mlp)
        solution = df.preprocessed_text_mlp

    if (solution == student).all():
        print(True)
    else:
        print("text_preprocessing_mlp(text) does not produce the expected result.")
        print(f"The rows with differences (up to 5) are shown below:")
        diff = df[solution != student][['cleaned_text', 'preprocessed_text_mlp']]
        diff['your_output'] = student[solution != student]
        print(diff.head(5).to_string(index=False))