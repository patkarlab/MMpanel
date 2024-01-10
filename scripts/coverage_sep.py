#!/usr/bin/env python
# This script will take 1. bed file in csv format 2. one set of regions to separate

import sys

combined_bedfile = sys.argv[1]		# Input coverage file
cnv_probes = sys.argv[2]			# File containing one set of probes
