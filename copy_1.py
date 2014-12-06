#!/usr/bin/env python
# -*- coding: utf-8 -*-



import re
import sys


fasta_file = sys.argv[1]
#aim_domain_1 = sys.argv[1]
#aim_domain_2 = sys.argv[3]


domain1= ['IP.LC', 'VP.LC']
domain2= ['CELQ.L','CTLQ.L','CKLQ.L']
domain3= ['C..C...C']
domain4= ['C..CGQC...C']
domain5= ['GEEFG']
domain6= 'ALRRLGF'
domain7= ['TIMEE','TVMEEG','TILEEG','TIWEEG','TVIEE','TIVEE','TIIEEG']
domain8= ['P..TSCCP.W','P..TSCSP.W','P..TTCCP.W','P..ASACP.W','P..TSACP.W']
domain9= 'F...GGV.E'
domain10= 'AA.RT'
domain11= ['E.MGC..GC..G.G','E.MAC..GC..G.G','E.MTC..GC..G.G','E.MCC..GC..G.G','E.MSC..GC..G.G']

file_object = open(fasta_file)
try:
        all_the_fasta = file_object.read( )
finally:
        file_object.close()

fastas = all_the_fasta.split('>')

for key1 in domain8:
#    print key1
    for fasta in fastas:
        count = 0
        if fasta.find('gi') <= 0:
            continue
        f = re.findall(key1,fasta)
        if len(f) > 0:
            print key1 + "    "  + fasta
        else:
            count += 1
    if len(domain8) == count:
        print fasta
