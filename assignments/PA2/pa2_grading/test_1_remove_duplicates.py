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
    print("Hidden test case 1: Test the function 'remove_duplicates'")
    with HiddenPrints():
        from COMP2211_PA2 import remove_duplicates

        # load hidden test data
        df = pd.read_csv("hidden_movies_data.csv")

        # get student's answer
        student = remove_duplicates(df)

    if not student.duplicated().any():
        print(True)
    else:
        duplicate = student[student.duplicated()]
        print(f"remove_duplicates(df) does not produce the expected result. Duplicates found:\n{duplicate}")