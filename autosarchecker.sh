#!/bin/bash
#author: Harun Resit Kirbiyik

for i in $(find -type f -iname '*.cpp' -o -iname '*.h')
do
	vera++ $i
done

