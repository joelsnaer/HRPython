userinput = ""
name = ""
number = ""
a_dict = {}
while userinput.lower() != "n":
    name = input("Name: ")
    number = input("Number: ")
    a_dict[name] = number
    userinput = input("More data (y/n)? ")
list_of_values = [(key, value) for key, value in a_dict.items()]
list_of_values.sort()
print(list_of_values)