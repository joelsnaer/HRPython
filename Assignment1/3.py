import math

x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line
# convert stings to int
x1 = int(x1_str)
y1 = int(y1_str)
x2 = int(x2_str)
y2 = int(y2_str)

x_dist = x1-x2
y_dist = y1-y2

d = math.sqrt(x_dist**2+y_dist**2)
print("d =",d)  # do not change this line
