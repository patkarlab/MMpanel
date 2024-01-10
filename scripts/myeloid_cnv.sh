#!/usr/bin/bash

input1=$1   #sample_list.csv
input2="/home/pipelines/MMpanel/scripts/cnvkit_cnvmyeloid/CNV_3072_hg19_RegionNames.txt"

for i in `cat ${input1}`
do
	python3 myeloid_cnv.py /home/pipelines/MMpanel/Final_Output/${i}/${i}.coverview_regions.csv ${input2} /home/pipelines/MMpanel/Final_Output/${i}/${i}.xlsx
done
