#!/bin/bash

function maximum {
	if [ $a -gt $b ]
	then
		echo "$a is greater than $b"
	else
		echo "$b is greater than $a"
	fi
}
read -p "Enter 1st number: " a
read -p "Enter 2nd number: " b
maximum $a $b
