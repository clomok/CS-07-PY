import os

file_name = input("Choose a filename: ")
file_name = ("04-L5 " + file_name)
os.system(r'ping 8.8.8.8 >> "' + file_name + '".txt"')
with open(file_name + ".txt","r") as file:
    if "ms" in file.read():
        print("You have an internet connection")
    else:
        print("You don't have an internet connection")
