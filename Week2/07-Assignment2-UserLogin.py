# Create a UName and Pwd in the code.

# Collect credentials from user as input

# match to see if the credentials are correct

s1 = "sdfsdf"
s2 = "sdfsdf"

if s1 == s2:
    print ("Strings are same ")
else :
    print ("Strings are different ")


u1 = "Hemant"
u2 = "Scott"
u3 = "Tim"

p1 = "romeo1"
p2 = "romeo2"
p3 = "romeo3"

x = input("Enter UName")
y = input("Enter Pswd")

if ((x == u1) and (y == p1)) :
    print ("User ", x, " signed in")
else :
    print("Unable to sign user ", x)

if x == u1 and y == p1 :
    print("START of TRUE")

    print ("User ", x, " signed in")


    print("End of TRUE")

else :
    print("Unable to sign user ", x)
    print("End of FALSE")

print("This is out of IF Statement")