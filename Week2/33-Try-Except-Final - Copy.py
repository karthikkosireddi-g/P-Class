import os

try :

    print("Start My Code")

    f1 = open("I:\\Python\\Class2-Projects\\NewFile.txt", "x")
    print("Done creating")

    f1 = open("I:\\Python\\Class2-Projects\\NewFile.txt", "w")
    f1.write("Line 1 on to a new file")
    f1.close()
    print("Done writing")

    f5 = open("I:\\Python\\Class2-Projects\\NewFile.txt", "r")
    f5.read()
    f5.close()
    print("Done reading")

    # newFilePath = "I:\\Python\\Class2-Projects\\NewFile.txt"
    # os.remove(newFilePath)
    # print("Done deleting")

    print("End My Code")

except FileExistsError:
    print("File already exists")

except FileNotFoundError:
    print("File does not exist")

except NameError:
    print("Name error occurred")

except:
    print("Error occurred")

finally:
    print("Irresptive of any error")

print("~~~~~~~~~~~~After Try Block")