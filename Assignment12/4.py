def merge_lists(list1, list2):
    list3 = list1 + list2
    tempset = set(list3)
    list3 = list(tempset)
    list3.sort()
    return list3

# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))