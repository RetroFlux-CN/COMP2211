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
