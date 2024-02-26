#! /usr/bin/bash

# The input is bedfile without the extension
bedfile=$1

awk 'BEGIN{OFS="\t"}{print $1,$2,$3,$4}' ${bedfile}.bed > ${bedfile}_form.bed
bedtools sort -i ${bedfile}_form.bed > ${bedfile}_sortd.bed
bgzip -c ${bedfile}_sortd.bed > ${bedfile}_sortd.bed.gz
tabix -p bed ${bedfile}_sortd.bed.gz
awk 'BEGIN{FS="\t";OFS=""}{print $1,":",$2,"-",$3}' ${bedfile}_sortd.bed > ${bedfile}_sortd_regions.txt   # For Platypus
/usr/lib/jvm/java-8-openjdk-amd64/bin//java -jar /home/programs/picard/build/libs/picard.jar BedToIntervalList I=${bedfile}_sortd.bed O=${bedfile}_sortd.interval_list SD=/home/reference_genomes/hg19_broad/hg19_all.dict
