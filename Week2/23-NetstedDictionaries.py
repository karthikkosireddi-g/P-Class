mc1 = 10
mc1 = {
        "name" : "MAC",
        "ip" : "1.2.3.4",
        "status" : "PINGING",
        "value1" : 1000,
        "val2" : 10.23234,
        "val3" : True,
        "val4" : False
        }

mc2 = {
        "name" : "Linux",
        "ip" : "1.2.3.2",
        "status" : "PINGING"
        }

mc3 = {
        "name" : "win",
        "ip" : "1.2.3.5",
        "status" : "PINGING",
        "v1" : 1,
        "v2" : True
        }

allMC = {
        "mc1" : {
            "name" : "MAC",
            "ip" : "1.2.3.4",
            "status" : "PINGING"
        },
        "mc2" : {
                "name" : "Linux",
                "ip" : "1.2.3.2",
                "status" : "PINGING"
        },
        "mc3" : {
                "name" : "win",
                "ip" : "1.2.3.5",
                "status" : "PINGING"
        }
    }

print(allMC)
print(allMC["mc2"])
print(allMC["mc2"]["name"])
