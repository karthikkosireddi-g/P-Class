# Key Value Pair
# no longer worry about INDEX or POSITION
# get/update by Key of it
mc2 = {
    "name" : "MAC",
    "ip" : "1.2.3.4",
    "status" : "PINGING"
    }

mc2 = {
    "ip" : "1.2.3.4",
    "status" : "PINGING",
    "name": "MAC",
    "loc" : "PaloAlto",
    "DNS" : "A-record"
    }

mc1 = {"name" : "MAC", "ip" : "1.2.3.4", "status" : "PINGING"}


print(mc1)
print(type(mc1))
print(mc1["status"])

mc1["date"] = "12/10"
print(mc1)
print(mc1["date"])

mc1.pop("status")
print(mc1)