#!/bin/bash

mass=1
speed=3*10^8
Energy=$( bc << EOF
$mass*$speed*$speed
EOF
)
 echo "Energy was found to be $Energy"
