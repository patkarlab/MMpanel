#!/usr/bin/bash

R1=$1
R2=$2
VDJTOOLS="/usr/lib/jvm/java-11-openjdk-amd64/bin/java -Xmx20G -jar /home/programs/VDJtools/vdjtools-1.2.1/vdjtools-1.2.1.jar"
export R_LIBS="/home/tuhina/R/x86_64-pc-linux-gnu-library/3.6:$R_LIBS"

source activate new_base
mixcr align --species hsa ${R1} ${R2} output.vdjca
mixcr assemble output.vdjca output.clns
mixcr exportClones output.clns output.tsv

$VDJTOOLS Convert -S mixcr output.tsv ./
$VDJTOOLS CalcBasicStats -m ./metadata.txt ./cbs
##$VDJTOOLS CalcSegmentUsage -p -m ./metadata.txt ./
$VDJTOOLS CalcSpectratype -m ./metadata.txt ./

source deactivate
$VDJTOOLS PlotFancySpectratype output.txt ./
$VDJTOOLS PlotFancyVJUsage output.txt ./
$VDJTOOLS PlotSpectratypeV output.txt ./
