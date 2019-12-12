f1 = open("I:\Python\Class2-Projects\myFile.txt", "w") # opening in READ ONLY mode
f1.write("\n This is a new line")
f1.close()

f1 = open("I:\Python\Class2-Projects\myFile.txt", "r") # opening in READ ONLY mode
print(f1.read())
f1.close()

newFilePath = "I:\\Python\\Class2-Projects\\NewFile.txt"

import os
os.remove(newFilePath)

f100 = open("I:\\Python\\Class2-Projects\\NewFile.txt", "x")

f5 = open("I:\\Python\\Class2-Projects\\NewFile.txt", "r")
f5.read()
f5.close()