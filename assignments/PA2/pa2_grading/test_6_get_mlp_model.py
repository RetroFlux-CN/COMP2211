import sys
import os

import numpy as np
import pandas as pd
import keras
from keras.layers import Input, Dense, Dropout, Embedding, Conv1D, GlobalMaxPooling1D

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
    print("Hidden test case 6: Test the function 'get_mlp_model'")
    with HiddenPrints():
        from COMP2211_PA2 import get_mlp_model

        student_model = get_mlp_model()
        submitted_model = keras.models.load_model('mlp_model.keras')

        # check layer types
        allowed_layers = (Dense, Dropout)
        all_allowed = all(isinstance(layer, allowed_layers) for layer in student_model.layers)

        # want to check first layer is Input layer but Input layer does not appear in model.layers

        # Check if the number of layers is the same
        same_architecture = True
        if len(student_model.layers) != len(submitted_model.layers):
            print("Different number of layers.")
            same_architecture = False
        else:
            for layer1, layer2 in zip(student_model.layers, submitted_model.layers):
                config1 = layer1.get_config()
                config2 = layer2.get_config()

                # Ignore the layer name differences
                config1['name'] = config1['name'].split('_')[0]
                config2['name'] = config2['name'].split('_')[0]

                if config1 != config2:
                    print("Layer configurations do not match:")
                    print(f"Student layer config: {config1}")
                    print(f"Submitted layer config: {config2}")
                    same_architecture = False

        # run the model on a dummy dataset to see if it works
        test_X = np.random.rand(10, 5000)
        test_y = np.random.randint(0, 2, size=(10,))
        submitted_model.evaluate(test_X, test_y)

    if all_allowed and same_architecture:
        print(True)
    if not all_allowed:
        print("The model returned by 'get_mlp_model()' contains disallowed layer types.")
    if not same_architecture:
        print("The architecture of the model returned by 'get_mlp_model()' does not match that of the submitted model.")