n = int(input("Input a natural number: ")) # Do not change this line
calc = int(2)
prime = True
# Fill in the missing code below
while n > calc:
    if n % calc == 0 and n != calc:
        prime = False
        break
    calc += 1
# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("!Prime")