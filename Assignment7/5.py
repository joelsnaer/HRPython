import string
# palindrome function definition goes here
def is_palindrome(in_str):
    for x in in_str:
        if x in string.punctuation or x == " ":
            in_str = in_str.replace(x, "")
        if x.isupper():
            in_str = in_str.replace(x, x.lower())
    if in_str == in_str[::-1]:
        return True
    else:
        return False
in_str = input("Enter a string: ")

is_palindrome(in_str)
# call the function and print out the appropriate message
if is_palindrome(in_str) == True:
    print("\"" + in_str + "\" is a palindrome.")
else:
    print("\"" + in_str + "\" is not a palindrome.")