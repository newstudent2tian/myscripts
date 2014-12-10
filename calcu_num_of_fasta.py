#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


fasta_file = sys.argv[1]

file_object = open(fasta_file)
try:
        all_the_fasta = file_object.read( )
finally:
        file_object.close()

fastas = all_the_fasta.split('\n>')

for fasta in fastas:
	cells = fasta.split(']\n')
	num = len(cells[1])
        print num
#	print num# cells[1]
#	if 150 < num:
#		print '>' + fasta
#	else:
#		continue
