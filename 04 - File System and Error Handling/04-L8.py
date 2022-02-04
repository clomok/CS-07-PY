import os

#usr = input("What is the username on your computer? ")
#base_location = ("C:\Users")
#location = (base_location + "\" +
#os.mkdir(r"C:\Users\" + usr +)

try:
    os.mkdir(r"C:\Users\clomo\Downloads\Cars")
except:
    print("This directory already exists")
with open(r"C:\Users\clomo\Downloads\Cars\Mustang.txt", "a+") as file:
    pass
path = input("Enter directory path: ")
file_name = input("Enter file name: ")
new_name = input("Enter a new name: ")
os.system(r"copy {}\{} {}\{}".format(path, file_name, path, new_name))

#Cannot get it to complete the task it was designed for.
#What is the purpose of asking the path?
