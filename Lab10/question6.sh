#!/bin/bash
echo "Input a number: "
read n

if [ "$n" -gt 100 ]; then #Only a single [ bracket should be there in the beginning and end of the condition
	echo "The number is greater than 100."
else
	echo "The number is not greater than 100."
fi
if [ "$n" -gt 100 ]; then #Only a single [ bracket should be there in the beginning and end of the condition and also ; should be there
	echo "The number is greater than 100."
fi
