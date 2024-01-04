#!/usr/bin/bash
##BSUB -J smMIPS_pipeline
##BSUB -n 25
##BSUB -q normal
##-m cn2" to submit jobs to cn2
## or " -m cn3"

##########
#for ENTRY : BEDFILES#
##for LEUKEMIA/MIPS: /home/pipelines/mutation_detector_nextflow/bedfile/06112021_Leukemia_Panel_sorted
##for MIPS (IDT-MRD): /home/pipelines/mutation_detector_nextflow/bedfile/04243058_MRD_Panel_V1_final_sorted 
##for CNVpanel+ALP:/home/pipelines/mutation_detector_nextflow/bedfile/ALP_CNV_backbone_sorted
##for CNVpanel:/home/pipelines/mutation_detector_nextflow/bedfile/xgen-human-cnv-backbone-hyb-panel-probes
##for Lungpanel:/home/pipelines/mutation_detector_nextflow/bedfile/lung_panel_egfr_kras_tp53_sortd
##for Twistmyeloid:/home/pipelines/mutation_detector_nextflow/bedfile/Leukemia_Bed_file_MYFU_grch37_sorted
##for Twistlymphoid:/home/pipelines/mutation_detector_nextflow/bedfile/Leukemia_Bedfile_ALL_grch37hglft_genome_ucsc
##for combined_panel:/home/pipelines/mutation_detector_nextflow/bedfile/Leukemia_Panel_Myeloid_2023_Feb_hg37_sortd
##for multiple_myeloma:/home/pipelines/mutation_detector_nextflow/bedfile/myeloma_combined_sortd
##for CLL-IGVH : no bedfile required
##for multiple myeloma panel : --bedfile /home/pipelines/mutation_detector_nextflow/bedfile/myeloma_combined_tp53_nras_kras_sortd, --cnvkitRef /home/pipelines/NextSeq_mutation_detector_leukemia/scripts/cnvkit_mmpanel/Reference_combpanel.cnn
##for CNV myeloid panel : --bedfile /home/pipelines/mutation_detector_nextflow/bedfile/CNV_Small_hg19_newmyeloid_sortd, --cnvkitRef /home/pipelines/MMpanel/scripts/cnvkit_cnvmyeloid/Reference_combpanel.cnn, --gene_scatter_list /home/pipelines/MMpanel/scripts/cnvkit_cnvmyeloid



echo "WARNING : change the bedfile and the cnv reference"
# for cnvkit reference 
# 06112021_Leukemia_Panel_sorted.bed : "/home/pipelines/NextSeq_mutation_detector_leukemia/scripts/cnvkit_ref_GeneNames/Reference_labelled.cnn" 
# Leukemia_Panel_Myeloid_2023_Feb_hg37_sortd.bed : "/home/pipelines/NextSeq_mutation_detector_leukemia/scripts/cnvkit_combpanel/Reference_combpanel.cnn"

source activate new_base
nextflow -c /home/pipelines/NextSeq_mutation_detector_leukemia/nextflow.config run  main_mmpanel.nf -entry CLL \
--bedfile /home/pipelines/mutation_detector_nextflow/bedfile/Leukemia_Panel_Myeloid_2023_Feb_hg37_sortd \
--cnvkitRef /home/pipelines/NextSeq_mutation_detector_leukemia/scripts/cnvkit_combpanel/Reference_combpanel.cnn \
--sequences /home/pipelines/MMpanel/sequences/ \
--input /home/pipelines/MMpanel/samplesheet.csv \
-resume -bg
conda deactivate 

# For MM panel
#source activate new_base
#nextflow -c /home/pipelines/MMpanel/nextflow.config run main_mmpanel.nf -entry MIPS \
#--bedfile /home/pipelines/mutation_detector_nextflow/bedfile/myeloma_combined_tp53_nras_kras_sortd \
#--trans_bedfile /home/pipelines/MMpanel/bedfiles/MMPanel_translocation_sortd \
#--cnvkitRef /home/pipelines/NextSeq_mutation_detector_leukemia/scripts/cnvkit_mmpanel/Reference_combpanel.cnn \
#--sequences /home/pipelines/MMpanel/sequences/ \
#--input /home/pipelines/MMpanel/samplesheet.csv \
#-resume -bg

# For CNV myeloid panel
#source activate new_base
#nextflow -c /home/pipelines/MMpanel/nextflow.config run main_mmpanel.nf -entry MIPS \
#--bedfile /home/pipelines/mutation_detector_nextflow/bedfile/CNV_Small_hg19_newmyeloid_sortd \
#--trans_bedfile /home/pipelines/MMpanel/bedfiles/MMPanel_translocation_sortd \
#--cnvkitRef /home/pipelines/MMpanel/scripts/cnvkit_cnvmyeloid/Reference_combpanel.cnn \
#--gene_scatter_list /home/pipelines/MMpanel/scripts/cnvkit_cnvmyeloid \
#--sequences /home/pipelines/MMpanel/sequences/ \
#--input /home/pipelines/MMpanel/samplesheet.csv \
#-resume -bg
