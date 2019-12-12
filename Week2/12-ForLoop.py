
for i in range(10):
    print("%%%")
    print("!!!")

for j in range (20): # create a variable i, start with 0, go till i < 20 is true
    print(j)

s1 = "Sun and the Moon"
for charInString in s1:
    print(charInString)

k = 0
for s2 in s1:
    print(k, s2)
    k = k + 1


print(s2) # the last value is only left here now
print(s2[0])
print(s2[1])
print(s1[0])

print("end")