import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-20,20,1000)
f1=np.log(1/np.cos(x)**2)
f2=np.log(1/np.sin(x)**2)
plt.plot(x,f1,label='f1(x)')
plt.plot(x,f2,label='f2(x)')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Logarithmic Trigonometric Functions")
plt.legend()
plt.show()
#At x=npi/2, f1(x) becomes infinite and f2(x) becomes 0. Because 1000 sampled points rarely land exactly on the irrational values of pi/2, the curves do not show infinity. Instead, they show extremely sharp, high finite spikes.

