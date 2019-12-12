"""
# Banking Application

# 3 User's - uN, pwd, balance

# Create functions for
 # transfer
 # balance
 # add funds
 # userLoggedIn

# Make transfers between the 3 users
u1 = ["a", "pass01", 1400]
u2 = ["b", "pass02", 1300]
u3 = ["c", "pass03", 1200]
u4 = ["d", "pass04"]
"""
allUID = [1, 2, 3, 4]
allUsers = ["a", "b", "c", "d"]
allPass = ["pass01", "pass02", "pass03", "pass04"]
allBal = [2400, 1300, 1200, 1000000]

def getBalance(userName):
    i = 0
    for y in allUsers:
        if y == userName:
            print(allBal[i])
            return allBal[i]
            print("will never get executed")
        else :
            i += 1 # to go to the next user
def addFunds(userName, amount):
    i = 0
    for y in allUsers:
        if y == userName:
            allBal[i] += amount
            print("Done adding funds")
        else :
            i += 1 # to go to the next user

def transferFunds(userNameFrom, userNameTo, amount):
    i = 0
    for y in allUsers:
        if y == userNameFrom:
            allBal[i] -= amount
            print("Done removing funds from ", userNameFrom)
        else :
            i += 1 # to go to the next user

    i = 0
    for y in allUsers:
        if y == userNameTo:
            allBal[i] += amount
            print("Done adding funds to ", userNameTo)
        else :
            i += 1 # to go to the next user

############### MAIN CODE
"""
print(getBalance("a"))
print(getBalance("b"))
print(getBalance("c"))

addFunds("c", 20)
print(getBalance("c"))

transferFunds("a","c", 1000)
print(getBalance("a"))
print(getBalance("c"))

"""

# User Login
# User does transactions

def logUserIn(uN, pW):
    pos = 0
    for euN in allUsers:
        # print("User Name comparing with is ", uN)
        # print("User Pswd ccomparing with is ", allPass[pos])
        if (uN == euN):
            print("Reached the position of user name")
            if (pW == allPass[pos]):
                print("User ", uN, " signed in")
                print("So now the user can perform the actions")
                return "Success"
            else:
                return "Failure"
        pos += 1

i = 3
while i > 0 :
    x = input("UName")
    y = input("Pwd")
    if logUserIn(x, y) == "Success":
        print("User ", x, " has logged in.")
        task = 0
        while task != "E":
            task = input("Select a task. A--Add, B--Bal, T--Transfer, E--EndTransaction")
            if task == "A":
                amountToAdd = float(input("Amount of funds to add as a number"))
                addFunds(x,amountToAdd)
            elif task == "B":
                getBalance(x)
            elif task == "T":
                userToTransfer = input("Transfer to user? ")
                amountToTransfer = float(input("Amount of funds to transfer? "))
                transferFunds(x, userToTransfer, amountToTransfer)
            elif task == "E":
                print("thank you")
                break
        break
    else:
        i -= 1
        print("Incorrect Pswd for user ", x)
        print("Try again. You have ", i, " attempts left.")