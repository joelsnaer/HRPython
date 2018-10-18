from operator import itemgetter
def get_csv_data(file):
    try:
        with open(file, "r") as csvdata:
            table_data = [ line.split(";") for line in csvdata]
        return table_data
    except FileNotFoundError:
        print ("Cannot find file",file)
        return None

def country_sort(csvdata):
    country_dict = {}
    country_total_elo = {}
    for line in csvdata:
        country = line[2].strip()
        if country not in country_dict:
            country_dict[country] = 1
            country_total_elo[country] = int(line[3])
        elif country in country_dict:
            country_dict[country] += 1
            country_total_elo[country] += int(line[3])
    return sorted(country_dict.items()), sorted(country_total_elo.items())

def print_header():
    print("Players by country:")
    print("-------------------")

def print_result_country(csvdata):
    sorted_csvdata = sorted(csvdata,key=itemgetter(2))
    num = 0 
    playernumber = 0
    country_list, country_elo_list = country_sort(csvdata)
    for country in country_list:
        print("{} ({}) ({}):".format(country[0], country[1], round(int(country_elo_list[num][1]) / int(country[1]),1)))
        for x in range(country[1]):
            lastname, firstname = sorted_csvdata[playernumber][1].split(",")
            firstname.strip()
            lastname.strip()
            fullname = firstname + lastname
            print("{:>40}{:>10d}".format(fullname, int(sorted_csvdata[playernumber][3])))
            playernumber += 1
        num += 1

filename = input("Enter filename: ")
csvdata = get_csv_data(filename)
print_header()
if csvdata:
    print_result_country(csvdata)