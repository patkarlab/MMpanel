#!/usr/bin/bash 

samplesheet=$1

for i in `cat ${samplesheet}`
do 
	#nohup speedseq align -R "@RG\tID:id\tSM:${i}\tLB:lib" /home/reference_genomes/hg19_broad/hg19_all.fasta ../sequences/${i}_S*_R1_001.fastq.gz ../sequences/${i}_S*_R2_001.fastq.gz -o ${i} &
	nohup lumpyexpress -B ${i}_S*_R1_001.fastq.gz.bam -S ${i}_S*_R1_001.fastq.gz.splitters.bam -D ${i}_S*_R1_001.fastq.gz.discordants.bam -o ${i}.vcf &
done
