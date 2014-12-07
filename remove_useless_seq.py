#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
 
def restream_output(file_name):
	sys.stdout=open(file_name,'append')

file_name=sys.argv[1]
dmpname=sys.argv[2]

file_object = open(file_name)                                                                                               

try:                                                                                                                    
	all_the_text = file_object.read( )                                                                                 
finally:                                                                                                                
	file_object.close()              

seqs=all_the_text.split('\n>')
for seq in seqs:
	if seq.find(dmpname) > 0:
		print '>'+ seq
	else:
		continue
