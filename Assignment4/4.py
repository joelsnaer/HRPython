m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line
gcd = 0
for x in range (1, n):
    if m % x == 0 and n % x == 0:
        gcd = x
print(gcd)