#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
fasta_file = sys.argv[1]
file_object = open(fasta_file)
try:
    all_the_fasta = file_object.read( )
finally:
    file_object.close()
b=[]
result_last=[]
fastas = all_the_fasta.split('>')
result = []
for fasta in fastas:
# print fasta
  #  cells = re.findall('\[(.*?)\]',fasta )
    cells = fasta.split(']\n')
    namess = cells[0].split('[')
    names = namess[-1]
#    print cells
   # if len(cells) > 2:
    result.append(names)
#print result
c = set (result)
#print c
for j in c:
    same_name_file = []
    for fasta in fastas:
        if j in fasta:
            same_name_file.append(fasta)
    ret=''
    maxnum=0
    for single in same_name_file:
        seqs = single.split(']')
 #       print seqs
        seq = seqs[-1]
#        print seq
        if (len(seq) > maxnum):
            maxnum = len(seq)
            ret = single
        else:
            continue
    print ">" + single

