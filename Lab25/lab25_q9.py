import re
dna="ATCGCGAATTCAC"
pattern=r'GAATTC'
if re.search(pattern,dna):
    print("ECoRI restriction site found")
else:
    print("ECoRI restriction site not found")