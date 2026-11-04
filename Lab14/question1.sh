#!/bin/bash

happy()
{
	n=$1
	while [ $n -ne 1 ] && [ $n -ne 4 ]
	do
		sum=0
		while [ $n -gt 0 ]
		do
			digit=$((n%10))
			sum=$((sum + digit * digit))
			n=$((n / 10))
		done
		n=$sum
	done
	if [ $n -eq 1 ]
	then
		echo "happy number"
	else
		echo "not a happy number"
	fi
}
echo "Enter a number: "
read num
result=$(happy $num)
echo "$result"
