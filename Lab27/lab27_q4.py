import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(3)
organisms = ["E. coli", "S. cerevisiae", "P. falciparum", "S. coelicolor"]
mean_gc = [51, 38, 19, 72] # approximate genome GC content, %
fig,ax=plt.subplots(2,2,sharex=True,sharey=True)
#sharex=True means that all 4 plots have the same x-axis scale and sharey=True means that all 4 plots have the same y-axis scale.
bins=(np.arange(0,101,2))
for i in range(4):
    gc=rng.normal(mean_gc[i],4,size=1000)
    row=i//2
    col=i%2
    ax[row,col].hist(gc,bins=bins,color='skyblue')
    ax[row,col].axvline(mean_gc[i],color='red',linestyle='--')
    ax[row,col].set_title(organisms[i]+"(Mean="+str(mean_gc[i])+"%)")
ax[1,0].set_xlabel("GC Content(%)")
ax[1,1].set_xlabel("GC Content(%)")
ax[0,0].set_ylabel("Frequency")
ax[1,0].set_ylabel("Frequency")
fig.suptitle("Genome GC Content Distribution")
plt.tight_layout()
plt.show()