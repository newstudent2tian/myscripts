#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


gi_list = sys.argv[1]
fasta_file = sys.argv[2]


file_object1 = open(gi_list)                                                                                               
try:                                                                                                                    
        gi_s = file_object1.readlines( )                                                                                 
finally:                                                                                                                
        file_object1.close() 



file_object2 = open(fasta_file)
try:
        all_the_fasta = file_object2.read( )
finally:
        file_object2.close()


for gi in gi_s:

	fasta_s = all_the_fasta.split('\n>')
	for fasta in fasta_s:
		cells = fasta.split('|')
		for cell in cells:
			if cell[1] == gi[0]:
				print '>'+ fasta
			else:
				continue
