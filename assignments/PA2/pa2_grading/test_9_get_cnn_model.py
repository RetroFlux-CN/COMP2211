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
    print("Hidden test case 9: Test the function 'get_cnn_model'")
    with HiddenPrints():
        from COMP2211_PA2 import get_cnn_model

        student_model = get_cnn_model(200)
        student_model.build(input_shape=(None, 200))
        submitted_model = keras.models.load_model('cnn_model.keras')

        # check layer types
        allowed_layers = (Dense, Dropout, Embedding, Conv1D, GlobalMaxPooling1D)
        all_allowed = all(isinstance(layer, allowed_layers) for layer in student_model.layers)

        # want to check first layer is Input layer but Input layer does not appear in model.layers

        # check first layer is Embedding layer
        first_layer_is_embedding = True
        if not isinstance(student_model.layers[0], Embedding):
            first_layer_is_embedding = False

        # check at least one Conv1D layer
        has_conv1d = any(isinstance(layer, Conv1D) for layer in student_model.layers)

        # check at least one GlobalMaxPooling1D layer
        has_global_max_pooling = any(isinstance(layer, GlobalMaxPooling1D) for layer in student_model.layers)

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
        test_X = np.random.randint(0, 600, size=(10, 200))
        test_y = np.random.randint(0, 2, size=(10,))
        student_model.evaluate(test_X, test_y)

    if all_allowed and same_architecture and first_layer_is_embedding and has_conv1d and has_global_max_pooling:
        print(True)
    if not all_allowed:
        print("The model returned by 'get_cnn_model()' contains disallowed layer types.")
    if not first_layer_is_embedding:
        print("The first layer of the model returned by 'get_cnn_model()' is not an Embedding layer.")
    if not has_conv1d:
        print("The model returned by 'get_cnn_model()' does not contain any Conv1D layer.")
    if not has_global_max_pooling:
        print("The model returned by 'get_cnn_model()' does not contain any GlobalMaxPooling1D layer.")
    if not same_architecture:
        print("The architecture of the model returned by 'get_cnn_model()' does not match that of the submitted model.")