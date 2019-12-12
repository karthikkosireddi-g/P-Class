# Give upto 3 attempts for a sign-in
u1 = "Hemant"
u2 = "Scott"
u3 = "Tim"

p1 = "romeo1"
p2 = "romeo2"
p3 = "romeo3"

i = 3
while (i > 0) :
    x = input("Enter UName")
    y = input("Enter Pswd")

    if (x == u1) and (y == p1):
        print("User ", x, " signed in")
        print("So now the user can perform the actions")
        break
    elif (x == u2) and (y == p2):
        print("User ", x, " signed in")
        print("So now the user can perform the actions")
        break
    elif (x == u3) and (y == p3):
        print("User ", x, " signed in")
        print("So now the user can perform the actions")
        break
    else:
        print("Unable to sign user ", x)
        print("You have ", i, " left")
        i -= 1

print("End")