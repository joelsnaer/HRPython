def make_new_row(new_row):
    row = []
    if new_row == [] or new_row == [1]:
        new_row.append(1)
    else:
        row.append(new_row[0])
        for j in range(len(new_row)-1):
            row.append(new_row[j]+new_row[j+1])
        row.append(new_row[-1])
        new_row = row
    return new_row
# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)
