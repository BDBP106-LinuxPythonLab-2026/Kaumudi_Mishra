import numpy as np
import matplotlib.pyplot as plt
genes = ["GAPDH", "ACTB", "TP53", "MYC", "EGFR"]
control = np.array([950, 1200, 310, 150, 420])
treated = np.array([940, 1180, 610, 75, 430])
x=np.arange(len(genes))
width=0.4
fig,ax=plt.subplots()
ax.bar(x-width/2, control, width, label='Control')
ax.bar(x+width/2, treated, width, label='Treated')
ax.set_xlabel("Genes")
ax.set_ylabel("Expression level")
ax.set_title("Gene expression: Control vs Treated")
ax.set_xticks(x,labels=genes)
ax.legend()
plt.show()
fold_change=treated/control
print("Fold Change:")
for i in range(len(genes)):
    print(genes[i],":",round(fold_change[i],2))

#TP53 gets roughly doubled with fold change (1.97) and MYC gets halved with fold change (0.5)