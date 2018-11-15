name = input("Input a name: ")
first_name = name.split(", ")[1]
last_name = name.split(", ")[0]
print(first_name[0].upper() + ".", last_name.capitalize())