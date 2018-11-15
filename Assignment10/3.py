# Your functions should appear here
def populate_list(the_list):
    userinput = ""
    while userinput != "exit":
        userinput = input('Enter value to be added to list: ')
        userinput = userinput.lower()
        if userinput != "exit":
            the_list.append(userinput)
    return the_list

def triple_list(the_list):
    return the_list*3
# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)
