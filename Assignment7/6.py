# Your function definition goes here
def fibonacci(n):
    num = 1
    num_old = 1
    num_new = 1
    while num < n:
        num_new, num_old, num = num_new + num_old, num_new, num + 1
    return num_new
n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here    
for x in range(n):  
    print(fibonacci(x), end=" ")