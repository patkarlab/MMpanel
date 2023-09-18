#! /usr/bin/bash 

samplesheet=$1

source activate new_base
for samples in `cat ${samplesheet}`
do
	echo $samples
	#mkdir -p Final_Output/$samples
	#mkdir -p /home/pipelines/NextSeq_mutation_detector_leukemia/${samples}/cnvkit

	/home/pipelines/NextSeq_mutation_detector_leukemia/scripts/cnvkit.sh Final_Output/${samples}/${samples}.final.bam /home/pipelines/NextSeq_mutation_detector_leukemia/scripts/cnvkit_mmpanel/Reference_combpanel.cnn /home/pipelines/MMpanel/${samples}/cnvkit/

	/home/pipelines/MMpanel/scripts/gene_scatter/custom_scatter_chrwise.py /home/pipelines/MMpanel/scripts/cnvkit_mmpanel/chrwise_list.txt /home/pipelines/MMpanel/${samples}/cnvkit/${samples}.final.cnr /home/pipelines/MMpanel/${samples}/cnvkit/${samples}.final.cns ${samples}

	#cp ${samples}gene_scatter.pdf /home/pipelines/NextSeq_mutation_detector_leukemia/${samples}/cnvkit/
	cp ${samples}gene_scatter.pdf /home/pipelines/MMpanel/Final_Output/${samples}/

	#cp /home/pipelines/NextSeq_mutation_detector_leukemia/${samples}/cnvkit/${samples}.final-scatter.png /home/pipelines/NextSeq_mutation_detector_leukemia/${samples}/cnvkit/${samples}.final-diagram.pdf /home/pipelines/NextSeq_mutation_detector_leukemia/Final_Output/${samples}/

	#rm -r ${samples}
	rm ${samples}gene_scatter.pdf
done
