def mutate_list(a_list, index_num, v):
    ''' Inserts v at index index_num in a_list'''
    a_list.insert(index_num, v)
    
def remove_ch(a_list, index_num):
    ''' Removes character at index_num from a_list'''
    a_list.pop(index_num)
    
def get_list():
    ''' Reads in values for a list and returns the list '''
    user_list = input("Enter values in list separated by commas: ")
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    return user_list

# Main program starts here
user_input = 0
index = 0
user_list = get_list()
print(user_list)
choice = input("Enter choice (m,r): ")
if choice == "m":
    user_input = input().split(',')
    mutate_list(user_list, int(user_input[0]), int(user_input[1]))
elif choice == "r":
    user_input = int(input())
    remove_ch(user_list, user_input)
print(user_list)