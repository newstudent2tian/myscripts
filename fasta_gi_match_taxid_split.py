#!/usr/bin/python                                          
# coding: utf-8
# Author zhufeng.wang


import os

import subprocess
import traceback
import sys 
import time

outlist={}
outcount={}
count=0
namelist={}

if len(sys.argv) != 3:
    print "Usage: %s fastafilename dmpfilename"%(sys.argv[0])
    exit(0)

fastaname=sys.argv[1]
dmpfile=sys.argv[2]

if not os.path.exists(fastaname):
    print "fasta file '%s' not existed"%(fastaname)
    exit(0)

if not os.path.exists(dmpfile):
    print "dmp file '%s' not existed"%(dmpfile)
    exit(0)

def restream_file(filename):
    sys.stdout = open(filename, "append")

def process():
    file_object = open(fastaname)
    try:
        all_the_text = file_object.read()
    finally: 
        file_object.close()                                                                                                                                 
    
    count=0
    giall = all_the_text.split("\n>")
    for gi in giall:
        gifs = gi.split("|")
        gif=gifs[4]
        ginum=gifs[1]
        
        end=gif.rfind("]")
        start=gif.rfind("[")
        if end==-1 or start==-1:
            name=gif
        else:
            name=gif[start:end+1]

        command="grep -w %s %s"%(ginum, dmpfile)
        try:
            detail_string=subprocess.Popen(command, stderr=subprocess.PIPE, shell=True,stdout=subprocess.PIPE)
            detail_string=detail_string.stdout.read()
        except exception:
            print exception
            
        gikinds=detail_string.split()
        if len(gikinds) == 0:
            continue
        gikind=gikinds[1] 
        if gikind not in outcount:
            outcount[gikind]=count+1
            namelist[gikind]=name
            count=count+1

#        if gikind in namelist:
#            namelist[gikind]+='\n'
#            namelist[gikind]+=name

        gifs = gi.split('\n')
        output=">%04d|%s\n"%(outcount[gikind],ginum)
        for i in range(1,len(gifs)):
            output+=gifs[i]
            output+="\n"

        if gikind in outlist:
            outlist[gikind]+=output
        else:
            outlist[gikind]=output


    filecount=1
    for mem in outlist:
        filename="fasta.seq.txt.%d"%(filecount)
        restream_file(filename)
        filecount=filecount+1
        print outlist[mem]
    
    restream_file("fasta.seq.man")
    for mem in outcount:
        print mem,outcount[mem], namelist[mem]
        print "\n"


process()
