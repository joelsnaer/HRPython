# while number is not negative
# run user input and take in numbers from user
# save first number user inputs
# if user inputs number bigger than current number save that number instead
# print biggest number
num_int = int(input("Input a number: "))    # Do not change this line
max_int = num_int
# Fill in the missing code
while num_int > 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int > max_int:
        max_int = num_int
print("The maximum is", max_int)    # Do not change this line
