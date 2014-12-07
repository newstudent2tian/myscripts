#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Usage(): find_domain.py       fasta_file         aim_domain         prefix


import re
import sys


fasta_file = sys.argv[1]
aim_domain = sys.argv[2]
prefix = sys.argv[3]


#X = ['A','R','D','C','Q','E','H','I','G','N','L','K','M','F','P','S','T','W','Y','V']

file_object = open(fasta_file)
try:
        all_the_fasta = file_object.read( )
finally:
        file_object.close()


fastas = all_the_fasta.split('>')

for fasta in fastas:
	f = re.findall(aim_domain, fasta)
#	print f


	if f.count(aim_domain) > 0:
		print '>' + prefix + fasta
	else:
		continue
	#	print '>' + fasta
