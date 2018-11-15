num1 = int(input("First number: ")) # Do not change this line
num2 = int(input("Second number: ")) # Do not change this line
num3 = int(input("Third number: ")) # Do not change this line

# Fill in the missing code below
if num1 >= num2 and num1 >= num3:
    max = num1
elif num2 >= num1 and num2 >= num3:
    max = num2
else:
    max = num3
#max = max(num1, num2, num3)
print("The maximum is: ", max) # Do not change this line