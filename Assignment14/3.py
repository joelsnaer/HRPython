def menu_selection():
    print("Menu: ")
    userinput = input("add(a), remove(r), find(f): ")
    return userinput

def execute_selection(choice, a_dict):
    if choice == "a":
        add_to_dict(a_dict)
    elif choice == "r":
        remove_from_dict(a_dict)
    elif choice == "f":
        find_key(a_dict)
    else: 
        print("Invalid choice.")

def add_to_dict(a_dict):
    key = input("Key: ")
    value = input("Value: ")
    if key in a_dict:
        print("Error. Key already exists.")
    else:
        a_dict[key] = value

def remove_from_dict(a_dict): 
    key = input("key to remove: ")
    if key in a_dict:
        a_dict.pop(key, None)
    else:
        print("No such key exists in the dictionary.")

def find_key(a_dict):
    key = input("Key to locate: ")
    if key in a_dict:
        print("Value: ", a_dict[key])
    else:
        print("Key not found.")

def dict_to_tuples(a_dict):
    list_of_values = [(key, value) for key, value in a_dict.items()]
    return list_of_values

# Do not change this main function
def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()