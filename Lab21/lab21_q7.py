def analyse_dna(sequence):
    def gc_content():
        gc=sequence.count('G')+sequence.count('C')
        return (gc/len(sequence))*100
    gc=gc_content()
    print("GC Content: ",gc,"%")
    if gc>50:
        print("GC rich sequence")
    else:
        print("AT rich sequence")
analyse_dna("ATGCTGACT")