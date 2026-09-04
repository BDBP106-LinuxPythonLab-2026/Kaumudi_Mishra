#!/bin/bash

while read -r col1 col2 col3
do
	echo "$col1  $col2  $col3"
done < data.txt
