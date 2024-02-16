import os

# CREATING NEW FILE //
# f = open("newfile.txt", "x")


# OPENS FILE AND WRITE
# f = open("newfile.txt", "w")
# f.write("Python is easy to learn!")

# READ THE FILE
f = open("newfile.txt", "r")
print(f.read())
f.close()

# ADD NEW TO FILE
# f = open("newfile.txt", "a")
# f.write("\nPython Intermediatedsadsad")


# f = open("newfile.txt", "r")
# print(f.read())
# f.close()


# RETURN CHARACTERS
# f = open("newfile.txt", "r")
# print(f.read(12))

# READ PER LINE
# f = open("newfile.txt", "r")
# print(f.readline())
# print(f.readline())

#OR USING LOOP TO READ PER LINE
# for x in f:
#     print(x)
# f.close()

# DELETING A FILE 
# if os.path.exists("newfile.txt"):
#     os.remove("newfile.txt")
# else:
#     print("The file does not exists")