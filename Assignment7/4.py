# is_prime function definition goes here
def is_prime(num):
    calc = 2
    if num == 2 or num == 3:
        return True
    while num > calc:
        if num % calc == 0 and num != calc:
            return False
        calc += 1
    return True
num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message
if is_prime(num) == True:
    print(num, "is a prime")
else:
    print(num, "is not a prime")