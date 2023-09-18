#! /usr/bin/env python3

import sys
import csv

infile_name = sys.argv[1]
map_file_name = sys.argv[2]
outfile = sys.argv[3]                   # Output file

output_file = open (outfile,'w')
map_dict = {}
swscore_dict = {}
family_dict ={}
classify_dict = {}
line_no = 0 
with open (infile_name,'r') as infile:
	for lines in infile:
		line_no = line_no + 1 
		# print (lines, end='')
		if (line_no > 3):
			gene_name = lines.split()
			if len(lines) > 0:
				sw_score = int (gene_name[0])
				var_id = gene_name[4]
				classify = gene_name[9]
				family = gene_name[10]
				map_dict[var_id] = 1
				swscore_dict[var_id] = sw_score
				classify_dict[var_id] = classify
				family_dict[var_id] = family
				# print (gene_name[0], 'this is a list')
				#print (sw_score, type(var_id), type (classify), type (family))
# print (map)

with open (map_file_name,'r') as mapfile:
	for lines in mapfile:
		line_info = lines.split()
		if len(line_info) > 0:
			if line_info[2] in map_dict:
				print (line_info[0], line_info[1], line_info[2], line_info[3], line_info[4], classify_dict[line_info[2]], family_dict[line_info[2]], swscore_dict[line_info[2]], file=output_file, sep="\t")
