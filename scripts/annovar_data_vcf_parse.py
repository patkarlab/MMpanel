#! /usr/bin/env python3
# This script will parse the annovar output and print the SVTYPE and PAIR_COUNT data to a new file

import sys
import csv
import re

csv_file = sys.argv[1]	# csv file from the merge_csv process
vcf_file = sys.argv[2]	# vcf file for annovar 
output = sys.argv[3]	# Output file

map_dict = dict()
map_id = dict()
map_alt = dict()
map_info = dict()
with open (vcf_file, 'r') as input_vcf:
	vcf_handle = csv.reader(input_vcf, delimiter="\t")
	for lines in vcf_handle:
		if '#' not in lines[0]:
			chr_vcf = lines[0]
			pos_vcf = lines[1]
			id_vcf = lines[2]
			ref_vcf = lines[3]
			alt_vcf = lines[4]
			info_vcf = lines[7]

			if re.search('[a-zA-Z]', str(chr_vcf)):
				chr_vcf = re.sub ("chr","", chr_vcf, flags = re.IGNORECASE)
				chr_vcf = re.sub ("X","23", chr_vcf, flags = re.IGNORECASE)
				chr_vcf = re.sub ("Y","y", chr_vcf, flags = re.IGNORECASE)

			vcf_id = str(chr_vcf) + ':' +''.join(str(pos_vcf))
			#print (vcf_id)
			map_dict[vcf_id] = 1
			map_id[vcf_id] = id_vcf
			map_alt[vcf_id] = alt_vcf	
			map_info[vcf_id] = info_vcf

outfile = open (output,'w')
with open (csv_file,'r') as vcf:
	csv_handle = csv.reader(vcf)
	header = next (csv_handle)      # Removing the header
	parse_column = header.index('Otherinfo1')
	print (str(header[:parse_column])[1:-1].replace("'",""),"SVTYPE", "PAIR_COUNT", "ID","ALT", "INFO",file=outfile, sep=",")
	for str_lines in csv_handle:
		chrom = str_lines[0]
		start = int(str_lines[1]) - 1
		ref = str_lines[3]

		parse_data = str_lines[parse_column]
		variant_data = parse_data.split()[10]
		svdata = variant_data.split(';')
		svtype = 'unk'
		pair_count = -1
		alt = '-'
		info_ = '-'
		id_ = '-'
		for values in svdata:
			if "SVTYPE" in values:
				svtype = values.split('=')[1]
			if "PAIR_COUNT" in values:
				pair_count = values.split('=')[1]

		if re.search('[a-zA-Z]', str(chrom)):
			chrom = re.sub ("chr","", chrom, flags = re.IGNORECASE)
			chrom = re.sub ("X","23", chrom, flags = re.IGNORECASE)
			chrom = re.sub ("Y","y", chrom, flags = re.IGNORECASE)

		vep_id = str(chrom) + ':' +''.join(str(start))
		#print (vep_id)
		if vep_id in map_dict:
			id_ = map_id[vep_id]
			alt = map_alt[vep_id]
			info_ = map_info[vep_id]
			print (id_, alt, info_, sep="\t")
		else:
			pass

		#print (type (header), type (str_lines))
		print (str(str_lines[:parse_column])[1:-1].replace("'",""), svtype, pair_count, id_, alt, info_,file=outfile, sep=",")
