#!/bin/bash

echo -n "Enter a file name: "
read file

if [ -f "$file" ]; then
if [ -x "$file" ]; then
	echo "File exists and is executable"
else 
	echo "File exists but is not executable"
fi
else
	echo "File does not exist"
fi
