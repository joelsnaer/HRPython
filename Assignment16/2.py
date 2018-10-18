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

def year_sort(csvdata):
    year_dict = {}
    year_total_elo = {}
    for line in csvdata:
        year = line[4].strip()
        if year not in year_dict:
            year_dict[year] = 1
            year_total_elo[year] = int(line[3])
        elif year in year_dict:
            year_dict[year] += 1
            year_total_elo[year] += int(line[3])
    return sorted(year_dict.items()), sorted(year_total_elo.items())

def print_header_country():
    print("Players by country:")
    print("-------------------")

def print_header_year():
    print("Players by birth year:")
    print("----------------------")

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

def print_result_year(csvdata):
    sorted_csvdata = sorted(csvdata,key=itemgetter(4))
    num = 0 
    playernumber = 0
    year_list, year_elo_list = year_sort(csvdata)
    for year in year_list:
        print("{} ({}) ({}):".format(year[0], year[1], round(int(year_elo_list[num][1]) / int(year[1]),1)))
        for x in range(year[1]):
            lastname, firstname = sorted_csvdata[playernumber][1].split(",")
            firstname.strip()
            lastname.strip()
            fullname = firstname + lastname
            print("{:>40}{:>10d}".format(fullname, int(sorted_csvdata[playernumber][3])))
            playernumber += 1
        num += 1

filename = input("Enter filename: ")
csvdata = get_csv_data(filename)
print_header_country()
if csvdata:
    print_result_country(csvdata)
    print()
    print_header_year()
    print_result_year(csvdata)