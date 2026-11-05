import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-6,6,1000)
sigma=[1,1.5,2]
for s in sigma:
    g=(1/(s*np.sqrt(2*np.pi)))*np.exp(-(x**2)/(2*s**2))
    plt.plot(x,g,label='sigma='+str(s))
plt.xlabel("x")
plt.ylabel("g(x)")
plt.title("Normalized Gaussian Functions")
plt.legend()
plt.show()
#Smaller standard deviation produces a narrower and taller curve while larger standard deviation produces a wide and flatter curve. All the 3 curves are centered to 0.