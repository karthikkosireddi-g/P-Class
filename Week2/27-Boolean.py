b1 = True # boolean
b1 = False

anythingCanBeBoolean = True

# boolean can

z1 = "True" # String
z2 = "False"

if b1:
    print("Boolean is true")
else:
    print("Boolean is false")

def addNum(x1, x2, x3):
    if x3 == (x1 + x2):
        return "True"
    else:
        return "False"

ret1 = addNum(25,95,120)
print(ret1)
ret2 = addNum(125,95,222)
print(ret2)

if ret1 == "True":
    print("addNum works")
else:
    print("addNum DOES NOT work")

if ret2 == "True":
    print("addNum works")
else:
    print("addNum DOES NOT work")

def addNumBoolean(x1, x2, x3):
    if x3 == (x1 + x2):
        return True
    else:
        return False

ret1 = addNumBoolean(25,95,120)
ret2 = addNumBoolean(125,95,222)

if ret1:
    print("addNum works")
else:
    print("addNum DOES NOT work")

if ret2:
    print("addNum works")
else:
    print("addNum DOES NOT work")