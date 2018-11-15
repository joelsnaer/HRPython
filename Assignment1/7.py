years_str = input("Years: ") # do not change this line
years_int = int(years_str)
secs_in_year = 31536000
seconds_total = secs_in_year * years_int
current_population = 307357870
birth = seconds_total // 7
death = seconds_total // 13
immigrant = seconds_total // 35
new_population = current_population - death + birth + immigrant
print("New population after", years_int, " years is ", int(new_population)) # do not change this line

