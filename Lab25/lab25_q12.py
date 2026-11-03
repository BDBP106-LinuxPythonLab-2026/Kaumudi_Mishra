import re
dna="ATCGCGYAATTCAC"
if re.search(r'[^ATGC]',dna):
    print("Ambiguous bases found")
else:
    print("No ambiguous bases found")
non_ambiguous=re.findall(r'[ATGC]',dna)
print("Non-ambiguous bases:","".join(non_ambiguous))