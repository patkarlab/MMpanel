
while getopts "s:b:c:" flag
do
	case "${flag}" in
		s) sample=${OPTARG};;
		b) bam=${OPTARG};;
		c) config_file=${OPTARG};;
	esac
done

#BAM=$PWD/$sample"/gatk38_processing"/$sample".final.bam"
echo $sample
echo $bam
printf '%s\t%s\t%s' "$bam" "500" "$sample" > $config_file
