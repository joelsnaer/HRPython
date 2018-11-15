# find_min function definition goes here
def find_min(first, second):
    if first < second:
        return first
    else:
        return second
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
# Call the function here
minimum = find_min(first, second)
print("Minimum: ", minimum)