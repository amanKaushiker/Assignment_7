dic = {
    "name": "Aman Kaushik",
    "profession": "Software Developer",
}

print(dic["name"])
print(dic.get("name"))
print(dic.get("name1"))  # ==> return "none" as output

print(dic.keys())  # ==> Return all the keys in the dicobject


for key in dic.keys():
    print("key : ", key, " &  value : ", dic[key])

for key, value in dic.items():
    print(key, " : ", value)
