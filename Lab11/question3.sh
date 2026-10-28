#!/bin/bash
str=$1
if [ -z "$str" ]
then
	echo "Operator z: String is empty"
else
	echo "Operator z: String is not empty"
fi
if [ -n "$str" ]
then
	echo "Operator n: String is not empty"
else
	echo "Operator n: String is empty"
fi
