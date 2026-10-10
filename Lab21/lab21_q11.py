from functools import reduce
words = ["Hi", "I", "am", "Kaumudi", "Priyadarshini", "Mishra"]
print(reduce(lambda x,y: x+" "+y, words))