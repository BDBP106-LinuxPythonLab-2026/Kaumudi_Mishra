import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(7)
length = rng.integers(50, 800, size=100) # amino acids
weight = length * 0.11 + rng.normal(0, 3, size=100) # kDa (about 110 Da per residue)
membrane = rng.random(100) < 0.3
fig,ax=plt.subplots()
ax.scatter(length[~membrane],weight[~membrane],color='blue',marker='o',alpha=0.5,label='Soluble proteins')
ax.scatter(length[membrane],weight[membrane],color='red',marker='^',alpha=0.5,label='Membrane proteins')
ax.set_xlabel("Protein length (amino acids)")
ax.set_ylabel("Molecular Weight (kDa)")
ax.set_title("Protein length vs Molecular weight")
ax.legend()
plt.savefig("protein_size.png",dpi=150)