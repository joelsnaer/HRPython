num = int(input("Input an int: ")) # Do not change this line
count = int(0)
number = int(0)
# Fill in the missing code below
while count < num:
    number += 1
    if number % 2 == 1:
        print(number)
        count += 1