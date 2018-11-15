my_int = int(input('Give me an int >= 0: '))
bstr = ''
quotient = my_int
while True:
    bstr += str(quotient%2)
    quotient = int(quotient / 2)
    if quotient == 0:
        break
bstr = bstr[::-1]
print("The binary of", my_int, "is", bstr)