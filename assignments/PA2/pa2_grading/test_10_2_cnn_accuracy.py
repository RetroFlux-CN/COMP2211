import sys
import os

import numpy as np
import pandas as pd
import keras

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
    print("Hidden test case 10.2: Evaluate the accuracy of the submitted CNN model (80%)")
    with HiddenPrints():
        student_model = keras.models.load_model('cnn_model.keras')
        hidden_X_cnn = np.load('hidden_X_cnn.npy')
        ground_truth = np.load('hidden_y.npy')

        prediction = student_model.predict(x=hidden_X_cnn)
        predicted_classes = (prediction > 0.5).astype(int).flatten()
        accuracy = np.mean(predicted_classes == ground_truth)
        
    if accuracy >= 0.8:
        print(True)
    else:
        print(f"Model accuracy is {accuracy}, which is below 0.8 on the hidden test set.")