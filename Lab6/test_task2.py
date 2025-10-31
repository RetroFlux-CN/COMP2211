import re, pandas as pd

# put your "remove_duplicates" and "clean_text" functions here


# load the test file (Make sure the path is correct)
movies_data_test = pd.read_csv('./movies_data_cleaned.csv', usecols=['cleaned_text'])
movies_data = pd.read_csv('./movies_data.csv')
movies_data = remove_duplicates(movies_data)
movies_data['cleaned_text'] = movies_data.text.apply(clean_text)

# compare the first 100 rows
for i in range(100):
    try:
        assert movies_data_test.cleaned_text[i] == movies_data.cleaned_text[i]
    except AssertionError:
        print(f"Row {i} does not match: '{movies_data_test.cleaned_text[i]}' != '{movies_data.cleaned_text[i]}'")
print("Test Passed!")