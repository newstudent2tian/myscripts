#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

file_name=sys.argv[1]
dmpname=sys.argv[2]

file_object = open(file_name)                                                                                               

try:                                                                                                                    
        all_the_text = file_object.read( )                                                                                 
finally:                                                                                                                
        file_object.close()              

count=0
seqs=all_the_text.split('\n>')
for seq in seqs:
	seq_length=0
	lines=seq.split('\n')
	for i in range(1,len(lines)):
		seq_length = seq_length + len(lines[i])
	if seq_length >=int(dmpname):
		for i in range(0,len(lines)):
			print lines[i]
#		count = count+1
	else:
		continue

#print "total sequences: %d"%(count)
