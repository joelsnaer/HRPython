import string
#build_wordlist() function goes here
def build_wordlist(infile):
    words = []
    for line in infile:
        for word in line.split():
            if word not in string.punctuation:
                words.append(word)
    return words

#find_unique() function goes here
def find_unique(word_list):
    temp_set = set(word_list)
    temp_list = list(temp_set)
    return temp_list
def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)  
    infile.close()  
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()