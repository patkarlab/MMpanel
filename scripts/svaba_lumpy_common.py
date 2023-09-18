#!/usr/bin/env python
# This script will take the svaba and lumpy output and print the common translocations
import csv
import sys
import os
import re

svaba_vcf = sys.argv[1]
lumpy_vcf = sys.argv[2]
common_output = sys.argv[3]
output_svaba = os.path.splitext(svaba_vcf)[0] + '.tsv'
output_lumpy = os.path.splitext(lumpy_vcf)[0] + '.tsv'
outfile_svaba = open (output_svaba,'w')
outfile_lumpy = open (output_lumpy, 'w')
outfile_common = open (common_output, 'w')

chrom_array = []
id_array = []
pos_array =[]
ID_array = []
ref_array =[]
with open (svaba_vcf,'r') as vcf:
	csv_handle = csv.reader(vcf, delimiter="\t")
	print ("svaba output", file = outfile_svaba, sep="\t")
	print ("CHROM", "POS","ID","REF", "ALT", "DISC_MAPQ", "NM", "LO",file = outfile_svaba, sep="\t")
	for str_lines in csv_handle:
		if '#' not in str_lines[0]:
			chrom = str_lines[0]
			pos = str_lines[1]
			ID = str_lines[2]
			ref = str_lines[3]
			alt = str_lines[4]
			qual = str_lines[5]
			filt = str_lines[6]
			inf = str_lines[7]
			format_list = str_lines[8].split(':')
			LO_index = format_list.index('LO')	# Extract the log odds index
			LO = float (str_lines[9].split(':')[LO_index])
			chrom = re.sub ("chr","", chrom, flags = re.IGNORECASE)
			chrom = re.sub ("X","x", chrom, flags = re.IGNORECASE)
			chrom = re.sub ("Y","y", chrom, flags = re.IGNORECASE)

			chrom_alt = alt.replace("[","")
			chrom_alt = chrom_alt.replace("]","")
			chrom_no = chrom_alt.split(':')[0].split('chr')[1]
			chrom_no = re.sub ("X","x", chrom_no, flags = re.IGNORECASE)
			chrom_no = re.sub ("Y","y", chrom_no, flags = re.IGNORECASE)
			if "PASS" in filt:
				if "IMPRECISE" not in inf:
					info_values = inf.split(';')
					disc_mapq = 0
					nm = -1 
					for values in info_values:
						if "DISC_MAPQ" in values:
							disc_mapq = int (values.split('=')[1])
						if values.startswith('NM'):
							nm = int (values.split('=')[1])						
					if disc_mapq >= 60 and nm == 0 and LO > 1 and chrom != chrom_no:
						print (chrom, pos, ID, ref, alt, disc_mapq, nm, LO, file = outfile_svaba, sep="\t")
						chrom_array.append(chrom)
						id_array.append(chrom_no)
						pos_array.append(pos)
						ID_array.append(ID)
						ref_array.append(ref)

#print (chrom_array, id_array)
with open (lumpy_vcf,'r') as vcf2:
	vcf_handle = csv.reader(vcf2, delimiter="\t")
	print ("\n\n", file = outfile_lumpy, sep="\t")
	print ("lumpy output", file = outfile_lumpy, sep="\t")
	print ("CHROM", "POS","ID","REF", "ALT", "SVTYPE", "SU", file = outfile_lumpy, sep="\t")
	print ("\n\n", file = outfile_common, sep="\t")
	print ("common to svaba and lumpy", file = outfile_common, sep="\t")
	print ("CHROM", "POS","ID","REF", "ALT", file = outfile_common, sep="\t")
	for lines in vcf_handle:
		if '#' not in lines[0]:
			chrom_vcf = lines[0]
			pos_vcf = lines[1]
			id_vcf = lines[2]
			ref_vcf = lines[3]
			alt_vcf = lines[4]
			qual_vcf = lines[5]
			filt_vcf = lines[6]
			inf_vcf = lines[7]
			info_vcf_values = inf_vcf.split(';')
			svtype = ""
			su = 0
			chrom_vcf = re.sub ("chr","", chrom_vcf, flags = re.IGNORECASE)
			chrom_vcf = re.sub ("X","x", chrom_vcf, flags = re.IGNORECASE)
			chrom_vcf = re.sub ("Y","y", chrom_vcf, flags = re.IGNORECASE)
			for values_vcf in info_vcf_values:
				if "SVTYPE" in values_vcf:
					svtype = values_vcf.split('=')[1]
				if "SU" in values_vcf:
					su = int(values_vcf.split('=')[1])

			if svtype == "BND" and su >= 50:
				chrom_vcf_alt = alt_vcf.replace("[","")
				chrom_vcf_alt = chrom_vcf_alt.replace("]","")
				chrom_vcf_no = chrom_vcf_alt.split(':')[0].split('chr')[1]
				chrom_vcf_no = re.sub ("X","x", chrom_vcf_no, flags = re.IGNORECASE)
				chrom_vcf_no = re.sub ("Y","y", chrom_vcf_no, flags = re.IGNORECASE)	

				if chrom_vcf != chrom_vcf_no:   # Removing the same chromosome translocation
					print (chrom_vcf, pos_vcf, id_vcf, ref_vcf, alt_vcf, svtype, su, file = outfile_lumpy, sep="\t")
					if chrom_vcf in chrom_array:
						#print (chrom_vcf, chrom_vcf_no)
						if chrom_vcf_no == id_array[chrom_array.index(chrom_vcf)]:
							#print (chrom_vcf, chrom_vcf_no)
							print (lines[0], pos_vcf, id_vcf, ref_vcf, alt_vcf, file = outfile_common, sep="\t")
						
					if chrom_vcf in id_array:
						#print (chrom_vcf, chrom_vcf_no)
						if chrom_vcf_no == chrom_array[id_array.index(chrom_vcf)]:
							print (lines[0], pos_vcf, id_vcf, ref_vcf, alt_vcf, file = outfile_common, sep="\t")
