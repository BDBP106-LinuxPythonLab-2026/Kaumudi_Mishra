def log_function_call(func):
    def wrapper(dna):
        print("Running DNA analysis ....")
        result=func(dna)
        print("GC%: ", result)
        print("Analysis complete!")
        return result
    return wrapper
@log_function_call
def gc_percentage(dna):
     gc=dna.count("G")+dna.count("C")
     return (gc/len(dna))*100
gc_percentage("ATGCGCTGCAGTC")