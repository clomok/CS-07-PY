
"""
word = "teet"

num = (1, 2, 3, 4)
#num = ('1','2','3','4')

for the in word:
    print(the, end=" ")

print()

for n in num:
    print(n, n, sep=",")

print()

for dumb in range(-5, 5):
    print(dumb)

#input("hit enter to exit the program")
"""
"""
word = ("sessions")
for x in word:
    if x == "s":
        print("Pass execute")
        pass
    print(x)

print()

for x in word:
    if x == "s":
        print("continue execute")
        continue
    print(x)
"""

#recursion example
count = 0

def recur(count):
    if count == 10:
        return

    print("*" * count)
    count += 1
    recur(count)

recur(count)