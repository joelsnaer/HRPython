import string

def get_word_list(fpointer):
    word_list = []
    for line in fpointer:
        for word in line.split():
            word = word.strip(string.punctuation)
            word_list.append(word)
    return word_list

def word_list_to_counts(word_list):
    wordCounts = {}
    for word in word_list:
        if word.lower() in wordCounts:
            wordCounts[word.lower()] += 1
        else:
            wordCounts[word.lower()] = 1
    return wordCounts

def dict_to_tuple(word_count_dict):
    list_of_values = [(key, value) for key, value in word_count_dict.items()]
    return list_of_values

def main():
    filename = input("Name of file: ")
    # Get a file pointer
    fpointer = open(filename)
    # Get a list of words from the file
    word_list = get_word_list(fpointer) 
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))
    
main()