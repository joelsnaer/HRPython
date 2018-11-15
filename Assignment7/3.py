# The function definition goes here
def in_range(num):
    if num > 1 and num < 555:
        return True
    else:
        return False
num = int(input("Enter a number: "))

# You call the function here
if in_range(num) == True:
    print(num, " is in range.")
else:
    print(num, " is outside the range!")