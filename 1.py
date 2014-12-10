#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  sys
import  re
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
    cells = re.findall('\[(.*?)\]',fasta )
   # print cells
    result.append(cells)
    print result
#c = set (cells)
#print c


