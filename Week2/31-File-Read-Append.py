f1 = open("I:\Python\Class2-Projects\myFile.txt", "r") # opening in READ ONLY mode

print(f1.read())

f1.close()

# Write on to the end of the file ... appending

f2 = open("I:\Python\Class2-Projects\myFile.txt", "a")
f2.write("\nis this going to the last line")
f2.writelines(["12",
              "13",
              "14"])
# f2.read()
f2.close()

f1 = open("I:\Python\Class2-Projects\myFile.txt", "r") # opening in READ ONLY mode

print(f1.read())

f1.close()