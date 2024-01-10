#!/usr/bin/bash
# This script will take an input samplesheet csv 

sample_list=$1

for sample in `cat ${sample_list}`
do
	zcat ${sample}ACLL_S*_R1_001.fastq.gz  ${sample}BCLL_S*_R1_001.fastq.gz | gzip -c > ${sample}_concat_CLL_S1_R1_001.fastq.gz ; zcat ${sample}ACLL_S*_R2_001.fastq.gz  ${sample}BCLL_S*_R2_001.fastq.gz  | gzip -c > ${sample}_concat_CLL_S1_R2_001.fastq.gz

done
