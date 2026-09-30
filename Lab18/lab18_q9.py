s="GTTTCGATTATAACG"
print("From 1st position")
for i in range(0,len(s)-1,3):
    print(s[i:i+3])
print("From 3rd position")
for i in range(2,len(s)-1,3):
    print(s[i:i+3])