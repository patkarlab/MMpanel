#!/usr/bin/env python
import sys

infile_name = sys.argv[1]		# Input file containing region names 
map_file_name = sys.argv[2]		# bed file with missing region names 

map_gene_names = {}
with open (infile_name,'r') as infile:
	for lines in infile:
		# print (lines, end='')
		gene_name = lines.strip().split("\t")
		if len(gene_name) > 0:
			region = gene_name[0]
			region_name = gene_name[1]
			map_gene_names [region] = region_name
			#print (map_gene_names)

with open (map_file_name, 'r') as mapfile:
	for line in mapfile:
		line_info = line.strip().split("\t")
		if len(line_info) > 0:
			chrom = line_info[0]
			start = line_info[1]
			end = line_info[2]
			name = line_info[3].split(";")
			region_id = chrom + ':' +''.join(start) + '-' + ''.join(end)

			if len (name) > 1:
				print (region_id, name[2], sep='\t')
			else:
				if region_id in map_gene_names:
					print (region_id, map_gene_names[region_id], sep='\t')
				else:
					print (region_id + "could not be mapped")
			#if line_info[0] in map:
			#	print (line_info[0])
			#print (chrom, start)
