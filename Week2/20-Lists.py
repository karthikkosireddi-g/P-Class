# List is a container to store data together.
# each item, does not have to be of same data type
u1 = ["a", "pass01", 1400]
u2 = ["b", "pass02", 1300]
u3 = ["c", "pass03", 1200]
u4 = ["d", "pass04"]

print(u1)
print(u1[0])
print(u1[1])
print(u1[2])

for i in range(10):
    print(i)

for i in range(2, 8):
    print(i)

for s in "sdfsdfsdf":
    print(s)

tempText = "sdfsdfsdf"
for s in tempText:
    print(s)

for l in u1:
    print(l)

print(l)

x = u1[0]
print(x)

x = u1[1]
print(x)

x = u1[2]
print(x)

for y in u4:
    print(y)

print(len(u4))

u4.append(2000)
print(u4)

u4.insert(1,"XYZ")
print(u4)

u4.remove('XYZ') # Finds and removes that value in the list
print(u4)

u4.insert(1,"XYZ")
print(u4)
u4.pop(1) # removes from the position/index ... doesnt care about what is inside it
print(u4)