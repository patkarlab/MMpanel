import pandas as pd
import os, sys
import re

args = sys.argv
sample = args[1]
filepath = args[2]
outfile = args[3]
cava_path = args[4]
coverview_path = args[5]
pindel_path = args[6]
cnvkit_path = args[7]
pharma_marker_path = args[8]

#csvfilenames=[filepath+sample+'.final.concat.csv',cava_path+sample+'.cava.csv',pindel_path,coverview_path,filepath+sample+'.artefacts.csv',cnvkit_path,pharma_marker_path]
csvfilenames=[cava_path+sample+'.cava.csv',pindel_path,coverview_path,filepath+sample+'.artefacts.csv',cnvkit_path,pharma_marker_path]

writer = pd.ExcelWriter(outfile)
for csvfilename in csvfilenames:
	if os.path.getsize(csvfilename) != 0:
		sheetname=os.path.split(csvfilename)[1]
		df = pd.read_csv(csvfilename)
		print('process file:', csvfilename, 'shape:', df.shape)
		new_sheet_name = os.path.splitext(sheetname)[0]
		new_sheet_name = re.sub (sample,"", new_sheet_name, flags = re.IGNORECASE)
		df.to_excel(writer,sheet_name=new_sheet_name, index=False)
writer.save()
