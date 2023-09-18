#! /usr/bin/bash

samplesheet=$1

for samples in `cat ${samplesheet}`
do
	#java -Xmx8G -jar /home/programs/picard/build/libs/picard.jar FastqToSam -F1 MM11_1P.fq.gz -F2 MM11_2P.fq.gz -O temp.bam -SM MM1
	#samtools view -c -f 1 temp.bam
	
	#bwa mem -M -t 20 /home/reference_genomes/hg19_broad/hg19_all.fasta MM11_1P.fq.gz MM11_2P.fq.gz > M11.sam
	#samtools view -bT /home/reference_genomes/hg19_broad/hg19_all.fasta M11.sam > M11.bam
	
	#samtools sort M11.bam > M11_sortd.bam
	#samtools index M11_sortd.bam 
	
	#/home/programs/manta-1.6.0.centos6_x86_64/bin/configManta.py --tumorBam Final_Output/${samples}/${samples}.sorted.bam --referenceFasta /home/reference_genomes/hg19_broad/hg19_all.fasta --callRegions /home/pipelines/mutation_detector_nextflow/bedfile/myeloma_combined_tp53_nras_kras_sortd.bed.gz --runDir Final_Output/${samples}/

	#/home/programs/manta-1.6.0.centos6_x86_64/bin/configManta.py --tumorBam Final_Output/${samples}/${samples}.sorted.bam --referenceFasta /home/reference_genomes/hg19_broad/hg19_all.fasta --runDir Final_Output/${samples}/

	#Final_Output/${samples}/runWorkflow.py
#	gunzip Final_Output/${samples}/results/variants/tumorSV.vcf.gz
#	gunzip Final_Output/${samples}/results/variants/candidateSV.vcf.gz
#	gunzip Final_Output/${samples}/results/variants/candidateSmallIndels.vcf.gz
#
#	perl /home/programs/annovar_latest/annovar/convert2annovar.pl -format vcf4 Final_Output/${samples}/results/variants/tumorSV.vcf --outfile Final_Output/${samples}/results/variants/${samples}.tumorSV.avinput --withzyg --includeinfo
#	perl /home/programs/annovar_latest/annovar/convert2annovar.pl -format vcf4 Final_Output/${samples}/results/variants/candidateSV.vcf --outfile Final_Output/${samples}/results/variants/${samples}.candidateSV.avinput --withzyg --includeinfo
#
#	perl /home/programs/annovar_latest/annovar/table_annovar.pl Final_Output/${samples}/results/variants/${samples}.tumorSV.avinput --out Final_Output/${samples}/results/variants/${samples}.tumorSV --remove --protocol refGene,cytoBand,cosmic84,popfreq_all_20150413,avsnp150,intervar_20180118,1000g2015aug_all,clinvar_20170905 --operation g,r,f,f,f,f,f,f --buildver hg19 --nastring '-1' --otherinfo --csvout --thread 10 /home/programs/annovar_latest/annovar/humandb/ --xreffile /home/programs/annovar_latest/annovar/example/gene_fullxref.txt
#
#	perl /home/programs/annovar_latest/annovar/table_annovar.pl Final_Output/${samples}/results/variants/${samples}.candidateSV.avinput --out Final_Output/${samples}/results/variants/${samples}.candidateSV --remove --protocol refGene,cytoBand,cosmic84,popfreq_all_20150413,avsnp150,intervar_20180118,1000g2015aug_all,clinvar_20170905 --operation g,r,f,f,f,f,f,f --buildver hg19 --nastring '-1' --otherinfo --csvout --thread 10 /home/programs/annovar_latest/annovar/humandb/ --xreffile /home/programs/annovar_latest/annovar/example/gene_fullxref.txt

#	./scripts/annovar_data_parse.py Final_Output/${samples}/results/variants/${samples}.candidateSV.hg19_multianno.csv Final_Output/${samples}/results/variants/${samples}_candidateSV_annovar.csv
#	cp Final_Output/${samples}/results/variants/${samples}_candidateSV_annovar.csv ./

	/home/nikhil/programs/svaba/bin/svaba run -t Final_Output/${samples}/${samples}.sorted.bam -G /home/reference_genomes/hg19_broad/hg19_all.fasta -p 30 -k /home/pipelines/MMpanel/bedfiles/MMPanel_translocation_sortd.bed -D /home/reference_genomes/dbSNPGATK/dbsnp_138.hg19.vcf -a Final_Output/${samples}/${samples}_svaba

done
