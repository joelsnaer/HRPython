def to_list(the_string):
    the_list = []
    all_words = the_string.split(',')
    if len(all_words) == 1:
        all_words = the_string.split(' ')
    for words in all_words:
        the_list.append(words)
    return the_list
# The main program starts here - DO NOT change it
the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)