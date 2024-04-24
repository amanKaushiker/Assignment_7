countries = ("USA", "Russia", "China", "India")

temp = list(countries)  # ===> Convert tupple into list

print(temp)


# ===> To perform modifications on tupple we need to convert it into list and thn convert back into tupple

temp.append("Japan")
temp.pop()
temp[1] = "Finland"
countries = tuple(temp)
print("Upadted Countries : ", countries)
