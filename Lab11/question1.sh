#!/bin/bash
ls -l . newdir
ls -l . newdir 1>presentfiles 2>filesnotpresent
#The successful output and error message are stored in 2 separate files i.e. presentfiles and filesnotpresent respectively
ls -l . newdir >listoffiles
#listoffiles contains the succesful directory listing while the error message appeared on the screen
