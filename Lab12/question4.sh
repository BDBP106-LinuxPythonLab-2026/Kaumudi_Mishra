#!/bin/bash

echo "2 3 5 7" > nums.txt
read -ra numbers < nums.txt
echo "The numbers in the array are: ${numbers[*]}"

for n in ${numbers[*]}
do
	product=$[$n*2]
	echo "The product of doubling $n is $product"
done
