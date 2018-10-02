#sort_list() function goes here
def sort_list(a_list):
    return a_list.sort()
def main():
    #loop to accept integers until a non-digit is entered goes here
    userinput = 0
    a_list = []
    while str(userinput).isdigit():
        userinput = input()
        if str(userinput).isdigit():
            a_list.append(int(userinput))

    ######Do not modify this part######
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    ######Do not modify this part######
    
main()