#!/bin/bash

echo "Name of script is $0"
echo "Number of arguments passed are $#"
echo "Arguments passed to the script are $@"
echo "Exit code is $?"

ListOfArguments=(echo $@)
echo ${ListOfArguments[*]}
