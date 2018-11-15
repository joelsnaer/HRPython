d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line
# Fill in the missing code below
if d1 <= 6 and d1 >= 1 and d2 <= 6 and d2 >= 1:
    if d1+d2 == 7 or d1+d2 == 11:
        print("Winner")
    elif d1+d2 == 2 or d1+d2 == 3 or d1+d2==12:
        print("Loser")
    else:
        print(d1+d2)
else:
    print("Invalid input")