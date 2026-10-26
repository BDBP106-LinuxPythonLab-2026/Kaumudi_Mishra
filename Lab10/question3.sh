#!/bin/bash

echo -n "Enter a file name: "
read file

if [ -f "$file" ]; then
	if [ -x "$file" ]; then
		echo "File exists and is executable"
	else 
		echo "File exists but is not executable"
	fi
	exit 200
else
	echo "File does not exist"
	exit 201
fi

# (i) If the echo output is generated and then if the command echo $? is run, then it will give the exit code of the last command.
# (ii) If the echo $? command is given after the if command, we will not get the output because the exit command terminate the script before it reach the line.
# (iii) No, the exit command stops the script instantly.
