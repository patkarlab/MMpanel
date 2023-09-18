#!/usr/bin/env python3
# This script requires a file containing chromosome position and names as input. eg: chr_list_all.txt

import matplotlib.backends.backend_pdf
from matplotlib import pyplot as plt
import re
import sys
import numpy as np

chr_list_file = sys.argv[1]	# file containing information to be plotted
cnr_file = sys.argv[2]		# .cnr file 
cns_file = sys.argv[3]		# .cns file
outfile = sys.argv[4]		# Name of the output file

output_pdf = outfile + "gene_scatter" + '.pdf'
pdf = matplotlib.backends.backend_pdf.PdfPages(output_pdf)
#output_file = open (outfile,'w')
i = 0
pattern = re.compile("#")
with open (chr_list_file) as file_input:
	for lines in file_input:
		remove_hash = pattern.match(lines)
		if not remove_hash:
			columns = lines.split()
			i = i + 1
			no_of_regions = len (columns[0].split(','))
			chr_start_stop_list = columns[0].split(',')
			band_list = columns[1].split(',')
			#print (chr_start_stop_list)
			#fig, axs = plt.subplots(nrows = 1, ncols = 2)
			X_axis_list = list()
			X_axis_values = list()
			Y_axis_list = list()
			x_tick_list = list()
			weights_list = list()
			start_val_list = list()
			stop_val_list = list()
			x_ticks_labels_list = list()
			cns_data_list = list()
			cns_log2_list = list()
			color_list = list()
			ci_chrstart_list = list()
			ci_chrend_list = list()
			title_list = list()
			x_index = 0
			for values in range(0, no_of_regions):
				chromosome = chr_start_stop_list[values].split(':')[0]
				chr_name = chr_start_stop_list[values].split(':')[0]
				chr_name = re.sub ("chr","", chr_name, flags = re.IGNORECASE)
				chr_name = re.sub ("X","x", chr_name, flags = re.IGNORECASE)
				chr_name = re.sub ("Y","y", chr_name, flags = re.IGNORECASE)
				start_val = int ((chr_start_stop_list[values].split(':')[1]).split('-')[0])
				stop_val = int ((chr_start_stop_list[values].split(':')[1]).split('-')[1])
				band_name = band_list[values]				
				#region_number = values + 1
				#x_tick_val = (region_number + (region_number - 1)) / 2
				#print (chr_name, start_val, stop_val,band_name)

				x_index_start = x_index
				tick_regions_list = list()
				band_name_list = list()
				exon_probe_number = 1
				with open (cnr_file) as cnr_input_file:
					next (cnr_input_file)	# Avoiding the headers
					for cnr_lines in cnr_input_file:
						antitarget = re.search( "Antitarget", cnr_lines, re.I)  # Removing the lines with Antitarget
						if not antitarget:
							cnr_chr = cnr_lines.split()[0]
							cnr_chr = re.sub ("chr","", cnr_chr, flags = re.IGNORECASE)
							cnr_chr = re.sub ("X","x", cnr_chr, flags = re.IGNORECASE)
							cnr_chr = re.sub ("Y","y", cnr_chr, flags = re.IGNORECASE)
							if cnr_chr == chr_name:
								cnr_start = int (cnr_lines.split()[1])
								cnr_end = int (cnr_lines.split()[2])
								if cnr_start >= start_val and cnr_end <= stop_val:
									x_index = x_index + 1
									x_val = int (( cnr_start  + cnr_end ) / 2)	
									log2 = float (cnr_lines.split()[5])
									weight = float (cnr_lines.split()[6]) * 50.0	# Scaling the size of points
									X_axis_values.append (x_val)
									X_axis_list.append (x_index)
									Y_axis_list.append (log2)
									weights_list.append (weight)
									color_list.append ('gray')
									tick_regions_list.append(x_index)										
									band_name_mod = band_name + '_' + str(exon_probe_number)

									#band_name_mod = band_name
									band_name_list.append(band_name_mod)
									exon_probe_number = exon_probe_number + 1 
									#print (cnr_start, cnr_end, log2)
	
								if cnr_end > stop_val:
									break
									
				if x_index > x_index_start:		# Plotting the ticks only if there are datapoints
					x_tick_val = ((x_index_start + 1) + x_index) / 2
					start_val_list.append(x_index_start + 1)
					stop_val_list.append (x_index)

					if no_of_regions > 1:
						x_tick_list.extend (tick_regions_list)
						x_ticks_labels_list.extend (band_name_list)
					else:
						x_tick_list.append (x_tick_val)
						x_ticks_labels_list.append (band_name)

				with open (cns_file) as cns_input_file:
					next (cns_input_file)
					for cns_lines in cns_input_file:
						cns_data_list = list()
						cns_chr = cns_lines.split()[0]
						cns_chr = re.sub ("chr","", cns_chr, flags = re.IGNORECASE)
						cns_chr = re.sub ("X","x", cns_chr, flags = re.IGNORECASE)
						cns_chr = re.sub ("Y","y", cns_chr, flags = re.IGNORECASE)
						if cns_chr == chr_name:
							cns_start = int (cns_lines.split()[1])
							cns_end = int (cns_lines.split()[2])
							cns_log2 = float (cns_lines.split()[4])
							for x_axis_vals in X_axis_values:
								if x_axis_vals >= cns_start and x_axis_vals <= cns_end:
									cns_data_list.append(X_axis_values.index(x_axis_vals) + 1)

							#if cns_end > stop_val:
							#	break

						if len(cns_data_list) > 0:
							#print ("X list values are", cns_data_list[0], cns_data_list[-1])
							ci_chrstart_list.append(cns_data_list[0])
							ci_chrend_list.append(cns_data_list[-1])
							cns_log2_list.append(cns_log2)

			if no_of_regions > 20 and no_of_regions <= 90 :	# default figsize is (6.4, 4.8)
				#plot_length = float ( no_of_regions / 4 )
				plot_length = 15
			elif no_of_regions > 90 and no_of_regions <= 150:
				plot_length = 18
			elif no_of_regions > 150:
				#plot_length = float ( no_of_regions / 7 )
				plot_length = 24
			else: 
				plot_length = 7

			#print (no_of_regions, plot_length)
			plt.figure (figsize=(plot_length, 5))
			plt.subplots_adjust(bottom=0.3)	# This helps to adjust the space below the labels

			if no_of_regions == 1:
				new_title = str(chromosome) + ':' + ' '.join( str(y) for y in band_list)
				#plt.title(' '.join( str(y) for y in band_list))
				plt.title(new_title)
			else:
				for gene_exons in band_list:
					gene = gene_exons.split('_')[0]
					if gene not in title_list:
						title_list.append(gene)
				#plt.title(', '.join(str(x) for x in title_list))
				#new_title = str(chromosome) + ':' + ' '.join( str(y) for y in title_list)
				new_title = str(chromosome)
				plt.title(new_title)

			plt.scatter (X_axis_list, Y_axis_list, s=weights_list, alpha=0.5, color=color_list)	# Scatter plot of the data points
			#plt.scatter (cns_data_list, cns_log2_list, color='orange')						# Scatter plot of the trendline
			if len(X_axis_list) > 0:
				xlower = X_axis_list[0] + 10000     	# Adding a buffer of 100000 for proper visualization
				xupper = X_axis_list[-1] + 10000
			else:
				xlower = xupper = 0

			ylower = -3								# Default values for y limit axis
			yupper = 3
			#print ("x limits are",X_axis_list[0], X_axis_list[-1])
			for ylist_values in Y_axis_list:
				if ylist_values < ylower:
					ylower = ylist_values
				if ylist_values > yupper:
					yupper = ylist_values

			plt.ylim (ylower, yupper)
			plt.axhline(y=0.0, color='black')						# Plotting the x-axis
			plt.axhline(y=0.5, color='red')							# Plotting lines at x=+-0.5
			plt.axhline(y=-0.5, color='red')

			for start_stop_vals in range (0, len (start_val_list)):
				plt.axvline(x=start_val_list[start_stop_vals], color='gray', linestyle='dashed')	# Plotting the segmentation line
				plt.axvline(x=stop_val_list[start_stop_vals], color='gray', linestyle='dashed')		

			for ci_line in range (0, len(ci_chrstart_list)):
				plt.plot ([ci_chrstart_list[ci_line], ci_chrend_list[ci_line]],[ cns_log2_list[ci_line], cns_log2_list[ci_line]], color='darkorange', linewidth=3, solid_capstyle='round')
				#print (ci_chrstart_list[ci_line],ci_chrend_list[ci_line], cns_log2_list[ci_line])

			plt.xticks(x_tick_list, x_ticks_labels_list, rotation='vertical', fontsize=7)
			#plt.xlabel('Position')
			plt.yticks(np.arange(ylower, yupper, 0.5))
			plt.ylabel('Copy ratio (log2)')
			output = outfile + "_cnv_" + str(i) + '.png'
			#plt.title(band_list)
			#pdf.savefig (plt.savefig(output, format = 'png', dpi = 300, transparent=True, bbox_inches='tight',pad_inches = 0))
			pdf.savefig()
			plt.close()
			#print ( X_axis_list, Y_axis_list, file=output_file)

		else:
			continue	
print ("The output file is", output_pdf)
pdf.close()
