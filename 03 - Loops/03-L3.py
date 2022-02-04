
counter = int(input("starting number"))
top_num = int(input("top number"))
secret = int(input("what is the secret number?"))
count_by = int(input("whats the increment?"))

while counter < top_num:
    counter += count_by
    if counter == secret:
        print("Found!")
        break
    else:
        print("Check {}".format(counter))