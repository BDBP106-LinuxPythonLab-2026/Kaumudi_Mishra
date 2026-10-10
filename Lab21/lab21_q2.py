Temp_C=list(map(int,input('Enter temperature in celsius').split()))
Temp_F=list(map(lambda t: round((t*1.8)+32, 2), Temp_C))
print(Temp_F)