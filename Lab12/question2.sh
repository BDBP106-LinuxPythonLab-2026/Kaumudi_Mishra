#!/bin/bash

n=0
while [ $n -lt 51 ]
do
	echo "$n"
	n=$[n+2]
done

for n in {0..50..2}
do
	echo "$n"
done
