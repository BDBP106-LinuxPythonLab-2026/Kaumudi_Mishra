test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
max_count=0
for key in test_dict:
    unique=set(test_dict[key])
    if len(unique)>max_count:
        max_count=len(unique)
print(key)
