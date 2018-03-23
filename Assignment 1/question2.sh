#!/bin/bash

if [ $# -eq 0 ];then
	echo "No Arguments Entered"
	exit
fi


if [ ! -f evenfile ]; then
	touch evenfile
fi

if [ ! -f oddfile ]; then
	touch oddfile
fi	


awk 'NR % 2== 0' $1 >> evenfile

awk 'NR % 2 != 0' $1 >> oddfile

