#!/bin/bash
#author: Harun Resit Kirbiyik

for i in $(find -type f -iname '*' -o -iname '*')
do
	echo $i
	chmod 777 $i
done
