#! /usr/bin/bash

samplesheet=$1

#source activate new_base
for samples in `cat ${samplesheet}`
do
#	fastqc -f bam /home/pipelines/MMpanel/Final_Output/${samples}/${samples}.final.bam --extract --outdir /home/pipelines/MMpanel/Final_Output/${samples}/
#	fastqc -f fastq sequences/${Sample}_*R1_*.fastq.gz sequences/${Sample}_*R2_*.fastq.gz --extract --outdir /home/pipelines/MMpanel/Final_Output/${samples}/

	#bedtools bamtobed -i /home/pipelines/MMpanel/Final_Output/${samples}/${samples}.sorted.bam > /home/pipelines/MMpanel/Final_Output/${samples}/${samples}.bed
    #bedtools coverage -counts -a /home/pipelines/MMpanel/bedfiles/MMPanel_translocation_sortd.bed -b /home/pipelines/MMpanel/Final_Output/${samples}/${samples}.bed > /home/pipelines/MMpanel/Final_Output/${samples}/${samples}.counts.bed

	echo -ne ${samples}'\t'; grep -v '#' /home/pipelines/MMpanel/Final_Output/${samples}/${samples}_insert_size_metrics.txt	| awk 'BEGIN{FS=OFS="\t"}NR==3{ print $1}'
	#echo -ne ${samples}'\t'; grep -v '#' /home/pipelines/MMpanel/Final_Output/${samples}/${samples}"_hsmetrics.txt" | awk 'BEGIN{FS="\t"; OFS="\t"}NR==3{ print $7,$8}'
done
