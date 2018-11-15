def input_vector(size):
    vector = []
    for i in range(size):
        vector.append(input("Element no {}: ".format(i+1)))
    return vector

def dot_product(vector1, vector2):
    result = 0
    for i in range(len(vector1)):
        result = result + (float(vector1[i])*float(vector2[i]))
    return result
# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))