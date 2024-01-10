#!/usr/bin/bash

for chr in {1..22} X Y; 
do
	grep chr$chr: regions.dat | awk '{printf "%s,", $1 ; if (NR % 100 == 0) print "" } END {print ""}' | sed 's/,$//g' >> probes.dat
done
