def magic(dd,mm,yyyy):
    yy=yyyy%100
    if mm*dd==yy:
        #print("Magic date")
        return True
    else:
        #print("Not a magic date")
        return False
"""
dd=int(input("Enter day"))
mm=int(input("Enter month"))
yyyy=int(input("Enter year"))
magic(dd,mm,yyyy)
"""
for year in range(1900,2001):
    for month in range(1,13):
        for day in range(1,32):
            if magic(day,month,year):
                print(day,month,year)
