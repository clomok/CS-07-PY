import os
import datetime

while True:
    print("Current directory: " + os.getcwd())
    new_dir_name = input("Choose a name for a new directory: ")
    os.mkdir(new_dir_name)
    os.chdir(new_dir_name)
    print("Current directory: " + os.getcwd())
    if new_dir_name: