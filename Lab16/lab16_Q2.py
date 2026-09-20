p=float(input("Enter principal: "))
r=float(input("Enter rate of interest per annum: "))
t=float(input("Enter time in years: "))

import math
simple_interest=(p*r*t)/100
amount=p+simple_interest

print(f'simple interest is {simple_interest:.2f}')
print(f'amount is {amount:.2f}')