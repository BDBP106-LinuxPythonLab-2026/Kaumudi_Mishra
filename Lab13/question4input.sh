#4
awk '$4=="PHE"' 1HK0.pdb | awk '{print $2}' > PHE_atoms.xyz

