# Your function definition goes here
upper = 0
lower = 0

def count_case(user_input):
    global upper
    global lower
    for x in user_input:
        if x.isupper():
            upper += 1
        elif x.islower():
            lower += 1
user_input = input("Enter a string: ")
# Call the function here
count_case(user_input)
print("Upper case count: ", upper)
print("Lower case count: ", lower)