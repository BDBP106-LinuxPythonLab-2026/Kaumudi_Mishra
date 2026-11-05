import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

temps = np.arange(20, 71, 5)
activity = np.array([12, 20, 35, 52, 70, 85, 92, 78, 45, 18, 5])
fig, ax=plt.subplots()
ax.plot(temps,activity,marker="o")
ax.set_xlabel("Temperature(oC)")
ax.set_ylabel("Activity")
ax.set_title("Activity vs Temperature")

opt_temps=temps[np.argmax(activity)]
print("Optimum temperature",opt_temps)

ax.axvline(x=opt_temps,color='red',linestyle='--')
ax.annotate("Optimum Temperature = 50oC.", xy=(opt_temps,92))

plt.show()
