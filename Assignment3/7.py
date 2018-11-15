count = int(0)
while count < 18:
    count += 1
    par = int(input("Par of hole " + str(count) + ": "))
    score = int(input("Score on hole " + str(count) + ": "))
    if score - 3 > par:
        print("bad hole")
    elif score + 3 == par:
        print("albatross")
    elif score + 2 == par:
        print("eagle")
    elif score + 1 == par: 
        print("birdie")
    elif score == par:
        print("par")
    elif score - 1 == par:
        print("bogey")
    elif score - 2 == par:
        print("double bogey")
    elif score - 3 == par:
        print("triple bogey")
    elif score - 3 < par:
        print("invalid score")