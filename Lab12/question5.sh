#!/bin/bash

function divide {
	local a=$1
	local b=$2
	if [ $b -eq 0 ]
	then
		echo "Division by zero cannot be done"
	else
		q=$(echo "scale=2; $a / $b" | bc)
		r=$((a%b))
		echo "Quotient=$q"
		echo "Remainder=$r"
	fi
}
read -p "Enter 1st number: " a
read -p "Enter 2nd number: " b
divide $a $b

