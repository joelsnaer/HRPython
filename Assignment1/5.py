secs_str = input("Input seconds: ") # do not change this line
time = int(secs_str)
hours = int(time // 3600)
time  %= 3600
minutes = int(time // 60)
time %= 60
seconds = time
print(hours,":",minutes,":",seconds) # do not change this line
