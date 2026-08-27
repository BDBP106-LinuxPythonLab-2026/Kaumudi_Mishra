#Q2(i)
awk '$2<25 {print}' question2.sh

#2(ii)
 awk '$3=="Physics" {print}' question2.sh

#2(iii)
awk '{print $1,",",$2,",",$3}' question2.sh > data2.csv

