def cell_metabolism(g,o):
    def energy_output():
        if o==6*g:
            nATP=38*g
        elif g>o//6:
            nATP=38*(o//6)
        else:
            nATP=38*g
        return nATP
    return energy_output()
print(cell_metabolism(2,18))
