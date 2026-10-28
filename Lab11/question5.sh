#!/bin/bash

#1
var1=Testing
var2=testing

#2
if [ $var1 \> $var2 ]; then
	echo "$var1 is greater than $var2"
else
	echo "$var1 is lesser than $var2"
fi

#3 Output is Testing is lesser than testing

#4 
echo -e "$var1\n$var2" > teststringfile

#5
sort "teststringfile"

#If statement output is Testing is lesser than testing whereas when using sort the output is testing is lesser than Testing. This is because in bash, uppercase letter values have lesser value than lowercase when comparing using ASCII comparision whereas sort method sorts it alphabetically, lower case first.

