class InvalidDNASequenceError(Exception):
    pass
class InvalidSiteError(Exception):
    pass

class DNASequence:
    def __init__(self,id,sequence):
        self.id=id
        self.sequence=sequence.upper()
        for base in self.sequence:
            if base not in "ATGC":
                raise InvalidDNASequenceError("Invalid DNA sequence")

    def complement(self):
        pairs={'A':'T','T':'A','G':'C','C':'G'}
        comp=""
        for base in self.sequence:
            comp=comp+pairs[base]
        return DNASequence(self.id+"_comp",comp)

    def reverse_complement(self):
        comp=self.complement()
        rev=comp.sequence[::-1]
        return DNASequence(self.id+"_revcomp",rev)

    def transcribe(self):
        mrna=self.sequence.replace("T","U")
        return mrna

    def find_site(self,site):
        site=site.upper()
        if site=="":
            raise InvalidSiteError("Site cannot be empty")
        for base in site:
            if base not in "ATGC":
                raise InvalidSiteError("Invalid DNA site")
        positions=[]
        for i in range(len(self.sequence)-len(site)+1):
            if self.sequence[i:i+len(site)]==site:
                positions.append(i+1)
        return positions

#Test code
s2=DNASequence("seq2","ATGGAATTCTAG")
print("Original:          ", s2.sequence)
print("Complement:        ", s2.complement().sequence)
print("Reverse complement:", s2.reverse_complement().sequence)
print("mRNA:              ", s2.transcribe())
print("GAATTC at:", s2.find_site("GAATTC"))
print("TTT at:", s2.find_site("TTT"))