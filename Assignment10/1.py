import string

sentence = input("Input a sentence: ")

# Here you should add the missing part
unique_letters = []
for letter in sentence:
    if letter not in unique_letters and letter.isalpha():
        unique_letters.append(letter)
print("Unique letters:", unique_letters)
