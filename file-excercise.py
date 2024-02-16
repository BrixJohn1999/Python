# f = open("excercise.txt", "w")

# f = open("excercise.txt", "r")
# print(f.read())
# f.close()
import os

if os.path.exists("excercise.txt"):
    os.remove("excercise.txt")
    print("Removing FIle")
else:
    print("The file does not exist")

