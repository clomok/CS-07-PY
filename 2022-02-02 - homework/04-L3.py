#Lab Task 1
"""
try:
    with open("04-L3-text.txt", "r") as text:
        text.write("Test")

except Exception:
    print("Unsupported Operation, cannot write in read mode.")
"""

#Lab Task 2
try:
    file = open("04-L3-file.txt", "a")
    while True:
        message = input("Enter Text! ('Exit' to exit): ")
        if message.lower() == "exit":
            break
        else:
            file.write(message + "\n")
    file.close()

except:
    print("An error occurred while trying to open the file.")