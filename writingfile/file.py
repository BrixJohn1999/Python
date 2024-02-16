# CREATING NEW FILE //
# f = open("newfile.txt", "x")

# OPENS FILE AND WRITE
f = open("newfile.txt", "w")
f.write("Python is easy to learn!")

# READ THE FILE
f = open("newfile.txt", "r")
print(f.read())
f.close()

# ADD NEW TO FILE
f = open("newfile.txt", "a")
f.write("\nPython Intermediate")


f = open("newfile.txt", "r")
print(f.read())
f.close()