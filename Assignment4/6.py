top_num = int(input("Upper number for the range: ")) # Do not change this line
intdiv = 0
for x in range(1, top_num+1):
    intdiv = 0
    for y in range(1, x):
        if x % y == 0:
            intdiv += y
    if intdiv == x:
        print(x)