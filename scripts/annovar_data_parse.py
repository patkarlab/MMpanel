#! /usr/bin/env python3
# This script will parse the annovar output and print the SVTYPE and PAIR_COUNT data to a new file

import sys
import csv
import re

csv_file = sys.argv[1]	# csv file from the merge_csv process
output = sys.argv[2]	# Output file

outfile = open (output,'w')
with open (csv_file,'r') as vcf:
	csv_handle = csv.reader(vcf)
	header = next (csv_handle)      # Removing the header
	parse_column = header.index('Otherinfo1')
	print (str(header[:parse_column])[1:-1].replace("'",""),"MATEID",,"SVTYPE", "PAIR_COUNT", file=outfile, sep=",")
	for str_lines in csv_handle:
		parse_data = str_lines[parse_column]

		variant_data = parse_data.split()[10]
		svdata = variant_data.split(';')

		mate_id = '-'
		svtype = 'unk'
		pair_count = -1
		for values in svdata:
			if "SVTYPE" in values:
				svtype = values.split('=')[1]
			if "PAIR_COUNT" in values:
				pair_count = values.split('=')[1]
			if "MATEID" in values:
				mate_id = values.split('=')[1]


		#print (type (header), type (str_lines))
		print (str(str_lines[:parse_column])[1:-1].replace("'",""), mate_id, svtype, pair_count, file=outfile, sep=",")
