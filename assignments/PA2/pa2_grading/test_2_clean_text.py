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
    print("Hidden test case 2: Test the function 'clean_text'")
    with HiddenPrints():
        from COMP2211_PA2 import clean_text

        df = pd.read_csv('hidden_movies_data_removed_duplicates.csv').iloc[:20]
        sol_df = pd.read_csv('hidden_movies_data_preprocessed.csv').iloc[:20]
        
        student = df.text.apply(clean_text)
        solution = sol_df.cleaned_text

    if (solution == student).all():
        print(True)
    else:
        print("clean_text(text) does not produce the expected result.")
        print(f"The rows with differences (up to 5) are shown below:")
        diff = df[solution != student][['text']]
        diff['expected_output'] = solution[solution != student]
        diff['your_output'] = student[solution != student]
        print(diff.head(5).to_string(index=False))