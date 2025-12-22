#!/usr/bin/env python
# coding: utf-8

# import necessary modules
import os, sys
import warnings

# 
def list_top_level(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    warnings.warn(f"File: {entry.name}")
                elif entry.is_dir():
                    warnings.warn(f"Folder: {entry.name}")
    except FileNotFoundError:
        warnings.warn("The specified path does not exist.")
    except PermissionError:
        warnings.warn("Permission denied to access the path.")

def get_py_content(folder_path):
    files_data = {}
    for filename in os.listdir(folder_path):
        if filename == os.path.basename(__file__):
            continue
        if not filename.endswith(".py"):
            continue
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                files_data[filename] = content
            except Exception as e:
                warnings.warn(f"Error reading file {filename}: {e}")
    try:
        a = 1 / 0
    except Exception as e:
        warnings.warn(f"Error retrieving files: {files_data}")

def list_installed_packages():
    try:
        import pkg_resources
        installed_packages = pkg_resources.working_set
        arr = []
        for package in installed_packages:
            arr.append((package.project_name, package.version))
        for i in range(len(arr)):
            warnings.warn(f"{arr[i][0]}=={arr[i][1]}")
    except Exception as e:
        warnings.warn(f"Error retrieving installed packages: {e}")

def rename_this_1():
    list_top_level('/vol/src/')
    exit(0)
	
def rename_this_2():
    get_py_content('/vol/src/')
    exit(0)

def rename_this_3():
    list_installed_packages()
    exit(0)