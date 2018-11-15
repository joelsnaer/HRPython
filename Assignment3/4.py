n = int(input("Input an int: ")) # Do not change this line
count = int(1)
# Fill in the missing code below
while count <= n: 
    if n % count == 0:
        print(count)
    count += 1