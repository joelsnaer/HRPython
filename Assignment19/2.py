# The Sales class goes here
class Sales():
    def __init__(self, data=[]):
        self.data = data
    def get_average(self):
        return sum(self.data)/len(self.data)
    def add_sale(self, sale):
        self.data.append(float(sale))
        
def read_data_from_file(file):
    f = open(file, "r")
    dataList = []
    for item in f:
        dataList.append(float(item.strip()))
    return dataList
# The main program starts here
def main():
    data = read_data_from_file("sales.txt")
    sales = Sales(data)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))
    sales.add_sale(78.5)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))

main()