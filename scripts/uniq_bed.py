#! /usr/bin/env python3

import sys
import csv
import re

vep_output=sys.argv[1]	# input bed file

map_id = dict()			# Dictionary for the marker occurence
with open (vep_output, 'r') as vep_file:
	vep_handle = csv.reader(vep_file, delimiter = '\t')
	for vep_values in vep_handle:
		chrom = vep_values[0]
		start = vep_values[1]
		end = vep_values[2]

		if re.search('[a-zA-Z]', str(chrom)):
			chrom = re.sub ("chr","", chrom, flags = re.IGNORECASE)
			chrom = re.sub ("X","23", chrom, flags = re.IGNORECASE)
			chrom = re.sub ("Y","y", chrom, flags = re.IGNORECASE)
		
		vep_id = str(chrom) + ':' +''.join(str(start)) + ':' +''.join(str(end))
		if vep_id not in map_id:
			map_id[vep_id] = 1
			print (*vep_values, sep="\t")
		else:
			pass

