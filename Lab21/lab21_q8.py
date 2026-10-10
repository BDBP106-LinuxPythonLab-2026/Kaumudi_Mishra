def protein_energy(temp):
    def calculate_free_energy(enthalpy,entropy):
        return enthalpy-temp*entropy
    h=float(input("Enter enthalpy value: "))
    s=float(input("Enter entropy value: "))
    g=calculate_free_energy(h,s)
    print("Free energy: ",g)
    if g<0:
        return "stable"
    else:
        return "unstable"
t=float(input("Enter temperature in kelvin: "))
print(protein_energy(t))