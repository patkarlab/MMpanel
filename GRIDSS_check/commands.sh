#! /usr/bin/bash

sample=$1
export R_LIBS="/home/tuhina/R/x86_64-pc-linux-gnu-library/3.6:$R_LIBS"
export R_LIBS="/home/vishram/R/x86_64-pc-linux-gnu-library/3.6:$R_LIBS"

export PATH="/home/programs/samtools-1.15.1:$PATH"
export PATH="/home/programs/gridss:$PATH"
export gridss_path="/home/programs/gridss"

# sed 's/^/chr/g' ENCFF001TDO.bed | grep -v 'chrM' > exclude_list.bed
# Call structural variants
gridss -r /home/reference_genomes/hg19_broad/hg19_all.fasta -j ${gridss_path}/gridss-2.13.2-gridss-jar-with-dependencies.jar -o ${sample}.vcf -b exclude_list.bed /home/pipelines/MMpanel/Final_Output/${sample}/${sample}.final.bam

# Call somatic structural variants
# This command was used to get the *breakpoint.bedpe and *breakend.bed files. These will be used as normals to compare with the samples.
/usr/lib/jvm/java-11-openjdk-amd64/bin/java -Xmx8g -cp /home/programs/gridss/gridss-2.13.2-gridss-jar-with-dependencies.jar gridss.GeneratePonBedpe $(ls -1 *.vcf | awk ' { print "INPUT=" $0 }') O=pondir/gridss_pon_breakpoint.bedpe SBO=pondir/gridss_pon_single_breakend.bed REFERENCE_SEQUENCE=/home/reference_genomes/hg19_broad/hg19_all.fasta NORMAL_ORDINAL=0
