
print("_"*50)
for i in range(100):
    print("|" + str(" "*(50-2)) + "|")
print("_"*50)

h = 30
w = 50

print("."*w)
for i in range(h):
    print("|" + str(" "*(w-2)) + "|")
print("."*w)


print("                *                ")
print("               ***               ")
print("              *****              ")
print("             *******             ")
print("            *********            ")
print("                *                ")
print("                *                ")
print("                *                ")
print("                *                ")
print("                *                ")

print(" "*16 + "*"*1 + " "*16)
print(" "*15 + "*"*3 + " "*15)
print(" "*14 + "*"*5 + " "*14)
print("              *****              ")
print("             *******             ")
print("            *********             ")
print("                *                ")
print("                *                ")
print("                *                ")
print("                *                ")
print("                *                ")

h = 30
w = 50
for i in range (int(h/2)):
    print(" "*(h/2-1) + "*"*(2*i-1) + " "*(h/2-1))
for i in range (int(h/2)):
    print(" "*(h/2-1) + "*" + " "*(h/2-1))
