# Take input from user (Mon, Tue, Wed ... )
# Print if it is weekend or not

x = input("Enter Day of the week")
"""
if (x == "Mon") :
    print ("Not a weekend")
elif (x == "Tue") :
    print ("Not a weekend")
elif (x == "Wed") :
    print ("Not a weekend")
elif (x == "Thu") :
    print ("Not a weekend")
elif (x == "Fri") :
    print ("Not a weekend")
elif (x == "Sat") :
    print ("HURRAY Weekend")
elif (x == "Sun") :
    print ("HURRAY Weekend")
else :
    print ("Did not recognize your entry")
"""


if x == "Sat" or x == "Sun":
    print("HURRAY Weekend")
else:
    print("Not a weekend")
