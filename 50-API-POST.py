import requests

j1 = {
    "name1": "morpheus",
    "job2": "leader"
    }

r1 = requests.post("https://reqres.in/api/users", j1)
print(r1.status_code)
print(r1.json())

j2 = {
    "name": "morpheus",
    "job": "zion resident"
    }

r2 = requests.put("https://reqres.in/api/users/2", j2)
print(r2.status_code)
print(r2.json())


# Tim added this line