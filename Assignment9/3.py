file = open("words.txt", "r")
longest_word = ""
for line in file:
    if len(line) > len(longest_word):
        longest_word = line
longest_word = longest_word.replace("\n", "")
print("Longest word is '" + longest_word + "' of length",len(longest_word))