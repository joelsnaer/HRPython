stars = int(input("Max number of stars: ")) # Do not change this line
for x in range(0, stars+1):
    for y in range (0, x):
        print("*", end='')
    print("")
for z in range(stars-1, -1, -1):
    for i in range(z, 0, -1):
        print("*", end='')
    print("")