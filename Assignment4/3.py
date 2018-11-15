sum = 0
number_of_grain = 1
for x in range(0, 64):
    sum += number_of_grain
    number_of_grain *= 2
print(sum)