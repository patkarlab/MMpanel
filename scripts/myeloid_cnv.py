#!/usr/bin/env python3

#myeloid_cnv.py 15AML229.coverview_regions.csv CNV_3072_hg19_RegionNames.txt 15AML229.xlsx
import os
import sys
import openpyxl
import csv
import pandas as pd


input1 = sys.argv[1]  #"15AML229.coverview_regions.csv"
input2 = sys.argv[2]  #"CNV_3072_hg19_RegionNames.txt"
input_xlsx_file = sys.argv[3]

#outfile1 = sys.argv[3] #cnv.csv
#outfile2 = sys.argv[4] #myeloid.csv

df1= pd.read_csv(input1, sep=",")
df2 = pd.read_csv(input2, sep="\t", header=None)
df2.columns = ["Location","Region"]

df3 = df2["Location"].str.split('[:-]', expand=True)
df3.columns = ["Chromosome", "Start_position", "End_position", "space"]
df3 = df3[["Chromosome", "Start_position", "End_position"]]

df3['Start_position'] = df3['Start_position'].astype(int)
df3['End_position'] = df3['End_position'].astype(int)
common_cnv = pd.merge(df1, df3, on=["Chromosome", "Start_position", "End_position"])
unique_cnv = common_cnv.drop_duplicates()

myeloid_cnv = pd.concat([df1, unique_cnv]).drop_duplicates(keep=False)


wb =openpyxl.load_workbook(input_xlsx_file)

with pd.ExcelWriter(input_xlsx_file, engine='openpyxl') as writer:
	writer.book = wb
	unique_cnv.to_excel(writer, sheet_name='CNV_coverview_region', index=False, header=True)
	myeloid_cnv.to_excel(writer, sheet_name='myeloid_coverview_region', index=False, header=True)


#xl_file = pd.read_excel(input_xlsx_file, sheet_name=None)
#with pd.ExcelWriter('output_temp.xlsx') as writer:
	#for sheet_names in xl_file.keys():
			#df = pd.read_excel(input_xlsx_file, sheet_name=sheet_names)
			#if  'Median coverage'in df:
				#df['Median coverage'] = df['Median coverage'].astype(str).astype(float)

			#df.to_excel(writer, sheet_name=sheet_names, index=False)

