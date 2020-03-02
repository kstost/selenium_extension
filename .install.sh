#!/bin/bash

if [ "$#" -eq 1 ]; then
	if [ -d $1 ]; then
	        cp .compare_current.sh $1
	        cp .find.sh $1
	        cp .install.sh $1
	        cp .list.sh $1
	        cp .manual.txt $1
	        cp .prepare_diff_source.py $1
	        cp .upload.sh $1
	        cp .x_check.sh $1
		echo 'install complete'
	fi
fi

