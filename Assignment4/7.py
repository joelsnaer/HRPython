top_num = int(input("Input a number between 0 and 999: "))

for x in range(0, top_num):
    length = len(str(x))
    sum = 0
    for y in str(x):
        sum += int(y) ** length
    if sum == x:
        print(x)