s1 = "   Welcome to the team PSE   "
s2 = "!!!Lets Python!!!"

print(s1)
print(type(s1))
print ("The length of the string is ", len(s1))

print(s1[0])
print(s1[22])
# print(s1[23])



print(s2.upper())
# print(s2.lower())

s2 = s2.upper()

if (s2.isupper()) :
    print ("YES they are upper case")
else :
    print ("NOPE. NOT UPPER.")

print(s1.strip()) # takes away extra spaces at the front end back.

print ("Position of !!! in s2 is at ", s2.index("!!!"))

print(s2.replace("!!!", "@@@"))
s2 = s2.replace("!!!", "@@@")


print (s2)
print("End of my program")