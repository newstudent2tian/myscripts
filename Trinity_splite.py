#!/usr/bin/python           
# -*- coding: utf-8 -*-     

import sys
import os

if(len(sys.argv) != 3):
     print 'Usage: Trinity.py filename splitnum'
     exit(0)                            


infilename=sys.argv[1]
splitnum=int(sys.argv[2])

file_object = open(infilename)
text=file_object.read()
segs=text.split('>')
segnum=len(segs)
index=0
seglen=segnum/splitnum+1

if(segnum < splitnum):
    print 'segment num is: %d, but you split it to: %d'%(segnum, splitnum)
    exit(0)

for segment in segs:
    if(index % seglen == 0):
        filename = infilename+'.%d'%(index / seglen)
        if os.path.isfile(filename):
            os.remove(filename)
        sys.stdout = open(filename, "append")
    print '>'+segment 
    index=index+1 
