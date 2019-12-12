# Print complete details of a PC

nIP = "10.11.12.13"
nName = "Dev01"
nUName = "AA"
nUPswd = "123qwe%$"
nHttpStatus = 200
nVersion = 13.456

print(type(nIP))
print(type(nHttpStatus))
print(type(nVersion))

print("IP Address : " + nIP)
# print("HTTP Status Address : " + nHttpStatus)
# print("Version Address : " + nVersion)

print("HTTP Status Address : ", nHttpStatus)
print("Version Address : ", nVersion)

print("HTTP Status Address : " + str(nHttpStatus))
print("Version Address : " + str(nVersion))

print("x", "y", "z")
print("x  ", "y  ", "z  ")
print("x" + "y" + "z")

print(type(nHttpStatus))
print(type(nVersion))

nHttpStatus = str(nHttpStatus)