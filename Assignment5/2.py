# Sequence is last 3 numbers added together make the next number
# While the n number of sequence numbers hasn't been printed
# print out first 3 numbers
# add the first three numbers into an array
# add number into array on position count where it is the sum of the past 3 numbers
# print out number
# raise count 
n = int(input("Enter the length of the sequence: ")) # Do not change this line
count = 3
sequence = [1, 2, 3]
print(sequence[0])
print(sequence[1])
print(sequence[2])
while count != n: # Á meðan count er ekki orðið n
    newnum = int(sequence[count-3]) + int(sequence[count-2]) + int(sequence[count-1])
    sequence.append(newnum)
    print(sequence[count])
    count += 1