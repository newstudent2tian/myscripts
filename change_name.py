#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
fasta_file = sys.argv[1]

file_object = open (fasta_file)
try:
    all_the_fasta = file_object.read()
finally:
    file_object.close()

fastas = all_the_fasta.split('>')
#print fastas
for fasta in fastas:
    if len(fasta) <= 0:
        continue
#    print fasta
    title_seq = fasta.split('|')
    if len(title_seq) <= 0:
        continue
#    print title_seq
    seq = title_seq[4].split("]\n")
#    print seq[0]
    species_name = seq[0].split('[')
#    print species_name
    if len(species_name[0]) <= 1:
        print '>' + title_seq[0] + '|' + title_seq[1] + '|' + species_name[2] + '\n' + seq[1]
    else:
        print '>' + title_seq[0] + '|' + title_seq[1] + '|' + species_name[1] + '\n' + seq[1]
