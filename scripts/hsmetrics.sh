#!/usr/bin/bash

file=$1				# Name of the file for adding the hsmetrics data for all samples
sample=$2			# Current sample's name
sample_hsmetrics=$3	# Current sample's hsmetrics.txt output

if [ -f ${file} ]; then
	counts=$(grep -wc ${sample} ${file})	# counting the occurence of sample id
	if [[ ${counts} -eq 0 ]]; then
		grep -v '#' ${sample_hsmetrics} | awk -v name=${sample} 'BEGIN{FS="\t"; OFS="\t"}NR==3{ print name,$7,$8}' >> ${file}
		echo "${sample} added to hsmetrics"
	fi
else
	echo -e "Sample name\tOn target\tOff target" > ${file}
	grep -v '#' ${sample_hsmetrics} | awk -v name=${sample} 'BEGIN{FS="\t"; OFS="\t"}NR==3{ print name,$7,$8}' >> ${file}
fi
