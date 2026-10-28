#!/bin/bash

function directory {
	dir=$1
	if [ -d "$dir" ]
	then
		echo "Directory exists"
		echo "Files in the directory are:" 
		ls "$dir"
	else
		mkdir "$dir"
		echo "Directory created successfully"
	fi
}
read -p "Enter directory name: " dir
directory "$dir"
