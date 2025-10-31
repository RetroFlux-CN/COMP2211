## Steps
1. download the files
2. open `test_task2.py` and copy the code to your notebook **or** put the functions code in `test_task2.py`   
3. put dataset files `.csv` to the corresponding folder
4. run the code to see the result 
If you have any problems, ask ofor help on the **Piazza**, not here.

If you see some weird characters in the output, change
```python
if not issue_found:
	print("\033[92mTest Passed!\033[0m")
else:
	print("\033[91mTest Failed!\033[0m")
```
to
```python
if not issue_found:
	print("Test Passed!")
else:
	print("Test Failed!")
```


Summary of my models:
MLP: Total params: 60,483 (236.26 KB)  89.7% on test dataset
CNN: Total params: 52,865 (206.50 KB)  82.6% on test dataset
I got 88.2% acc for mlp model, and 87.3% for cnn model on ZINC.

Do not ask anything about my code!
