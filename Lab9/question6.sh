#!/bin/bash

echo "The home variable is $HOME"

bcoutput=$( bc << EOF
scale=3
23934/44343
EOF
)
echo "23934/44343 is $bcoutput"

ls ~ | grep "D"

grep -i "IBAB" /etc/passwd
