import os
import sys

line = "<----------------------------------------------->"

system = sys.platform
print(f"you are using {system}")
root_folder = input("enter folder: ")

def mapper(path):
    try:
        for item in os.listdir(path):
            full_path = r"{}\{}".format(path,item)
            if os.path.isfile(full_path):
                size = os.stat(full_path).st_size
                print(f"found {full_path} size is {size} bytes")
            elif os.path.isdir(full_path):
                print(f"{line}\n entering folder {full_path}\n {line}")
                mapper(full_path)

            else:
                print("unkown")
    except Exception as error:
        print(error)
        global root_folder
        option = int(input("type 1 to enter another folder any other number to exit"))
        if option ==1:
            root_folder = input("enter another folder: ")
            mapper(root_folder)
        else:
            pass

mapper(root_folder)