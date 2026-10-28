#!/bin/bash
file=$1
#-e checks if a file exists or not
if [ -e "$file" ]
then
	echo "File exists"
else
	echo "File does not exists"
fi
#-s checks if a file is empty or not
if [ -s "$file" ]
then
	echo "File is not empty"
else
	echo "File is empty"
fi
#-f checks if a file is regular or not
if [ -f "$file" ]
then
	echo "It is a regular file"
else
	echo "It is not a regular file"
fi
