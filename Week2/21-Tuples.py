u1 = ["a", "pass01", 1400]
u2 = ["b", "pass02", 1300]
u3 = ["c", "pass03", 1200]
u4 = ["d", "pass04"]

allUID = [1, 2, 3]
allUsers = ["a", "b", "c"]
allPass = ["pass01", "pass02", "pass03"]
allBal = [2400, 1300, 1200]

allUsers[2] = "c-is-changed"
for uName in allUsers:
    print(uName)

allUsersTuple = ("a", "b", "c")
print (type(allUsersTuple))
for uName in allUsersTuple:
    print(uName)

allUsersTuple[2] = "d"
for uName in allUsersTuple:
    print(uName)

a = (1, 2, 3)
b = list(a)
print(b)
b[2] = 33333
print(b)
a = tuple(b)
