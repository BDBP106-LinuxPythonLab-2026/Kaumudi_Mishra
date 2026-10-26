#!/bin/bash
read -p "Enter your score in the range of 0-100: " s
if [ $s -ge 90 ] && [ $s -le 100 ]
then
	echo "Grade A"
elif [ $s -ge 80 ] && [ $s -lt 90 ]
then
	echo "Grade B"
elif [ $s -ge 70 ] && [ $s -lt 80 ]
then
	echo "Grade C"
elif [ $s -ge 0 ] && [ $s -lt 70 ]
then
	echo "Fail"
else
	echo "Invalid score"
fi
