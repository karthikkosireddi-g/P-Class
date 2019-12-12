u1 = "Hemant"
u2 = "Scott"
u3 = "Tim"

p1 = "romeo1"
p2 = "romeo2"
p3 = "romeo3"

def logUserIn(uN, pW, euN, epW):
    if (uN == euN) and (pW == epW):
        print("User ", uN, " signed in")
        print("So now the user can perform the actions")
        return "Success"
    else:
        return "Failure"

i = 3
while i > 0 :
    x = input("Enter UName")
    y = input("Enter Pswd")

    if logUserIn(x, y, u1, p1) == "Success":
        break
    elif logUserIn(x, y, u2, p2) == "Success":
        break
    elif logUserIn(x, y, u3, p3) == "Success":
        break
    else:
        print("Unable to sign user ", x)
        i -= 1
        print("You have ", i, " left")


