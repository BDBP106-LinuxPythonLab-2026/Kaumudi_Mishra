import re
dna="ACTNGCATRGCTACGTYACGATSCGAWTCG"
pattern=r'[^ATGC]'
result=re.split(pattern,dna)
result=[x for x in result if x!=""]
print(result)