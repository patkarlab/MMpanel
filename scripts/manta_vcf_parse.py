#! /usr/bin/env python3
# This script will parse the annovar output and print the SVTYPE and PAIR_COUNT data to a new file

import sys
import csv
import re

csv_file = sys.argv[1]	# csv file from the merge_csv process
output = sys.argv[2]	# Output file

outfile = open (output,'w')
with open (csv_file,'r') as vcf:
	csv_handle = csv.reader(vcf, delimiter="\t")
	print ("CHROM", "POS","ID","REF", "ALT","QUAL", "FILTER", "HOMSEQ","HOMLEN", "CIPOS","CIGAR","SVLEN","END","MATEID","SVTYPE", "PAIR_COUNT", "BND_PAIR_COUNT", "UPSTREAM_PAIR_COUNT", "DOWNSTREAM_PAIR_COUNT", file=outfile, sep="\t")
	for lines in csv_handle:
		if '#' not in lines[0]:
			chr_vcf = lines[0]
			pos_vcf = lines[1]
			id_vcf = lines[2]
			ref_vcf = lines[3]
			alt_vcf = lines[4]
			qual_vcf = lines[5]
			filter_vcf = lines[6]
			parse_data = lines[7]
			svdata = parse_data.split(';')
			
			downstream_pc = '-'
			upstream_pc = '-'
			bnd_pair_count = '-'
			homseq = '-'
			homlen = '-'
			cipos = '-'
			cigar = '-'
			svlen = '-'
			end = '-'
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
				if "END" in values:
					end = values.split('=')[1]
				if "SVLEN" in values:
					svlen = values.split('=')[1]
				if "CIGAR" in values:
					cigar = values.split('=')[1]
				if "CIPOS" in values:
					cipos = values.split('=')[1]
				if "HOMLEN" in values:
					homlen = values.split('=')[1]
				if "HOMSEQ" in values:
					homseq = values.split('=')[1]
				if "BND_PAIR_COUNT" in values:
					bnd_pair_count = values.split('=')[1]
				if "UPSTREAM_PAIR_COUNT" in values:
					upstream_pc = values.split('=')[1]
				if "DOWNSTREAM_PAIR_COUNT" in values:
					downstream_pc = values.split('=')[1]

			#print (type (header), type (str_lines))
			print (chr_vcf,pos_vcf,id_vcf,ref_vcf,alt_vcf,qual_vcf,filter_vcf, homseq, homlen, cipos, cigar, svlen, end, mate_id, svtype, pair_count, bnd_pair_count, upstream_pc, downstream_pc, file=outfile, sep="\t")
