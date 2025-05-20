#!/bin/bash

for file in Final_Output/*_R1.fastq.gz Final_Output/*_R2.fastq.gz; do
  # Skip if no files match
  [ -e "$file" ] || continue

  # Construct new filename by inserting _S01 before .fastq.gz
  newfile="${file/.fastq.gz/_S01.fastq.gz}"

  # Rename file
  mv "$file" "$newfile"
  echo "Renamed: $file → $newfile"
done
