num = 10
while num < 99:
    square = num * num
    if str(square)[1:] == str(num):
        print(num)
    num += 1