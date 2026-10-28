#!/bin/bash

read -p "Enter a number: " n

num=1
until [ $num -gt 15 ]
do
	p=$[ $n*$num ]
	echo "$n*$num=$p"
	num=$[num+1]
done	
