#!/bin/bash
val1=Jayashree
val2=Nagesh
#if [ $val1 > $val2 ]; then
#	echo "$val1 is greater than $val2"
#else
#	echo "$val1 is lesser than $val2"
#fi

if [ $val1 \> $val2 ]; then
	echo "$val1 is greater than $val2"
else
	echo "$val1 is lesser than $val2"
fi
#The latter script executes without creating a new file 
#The escape character "\" treats the greater than sign as an symbol and not the output redirection operator
