#!/usr/bin/env python
# -*- coding: utf-8 -*-
#感受：（1）了解二维数组的使用（2）注意每个变量放置的位置，如果没有放在正确的循环里，会导致奇怪的结果
#      （3）在编写程序之前要清晰的知道自己的目的，如，此程序的最终目的是要找到domain后将序列的名字更改成目的名字，终极目的是改名字，所以可以设置name空字符串，在找到后就更改名字，最终完成循环后，将序列加在名字后即可
import sys
import re

fasta_file = sys.argv[1]
#列出序列中所有可能的domain
domain1= ['IP.LC', 'VP.LC']
domain2= ['C..CGQC...CP']
domain3= ['CELQ','CEFQ','CTLQ','CELL','CKLQ']
#domain4= ['CRRC...C','CGRC...C','CGQC...C','CGVC...C','CNRC...C','CERC...C','CTRC...C','CDRC...C']
#domain3= ['TIMEE..E...R','TIVEE..E...R','TIIEE..E...R','TVIEE..E...R','TIWEE..E...R','TVMEE..E...R','TILEE..E...K']
#domain6= ['S..KSP..M','S..RSP..M','S..KSP..I','S..KSPQQ','A..KSPQQ']
#domain4= ['TIMEE','TVMEEG','TILEEG','TIWEEG','TVIEE','TIVEE','TIIEEG']
domain4= ['KC..C..C...C']
domain5= ['P..TSCCP.W','P..TTCCP.W','P..ASACP.W','P..TSACP.W']
domain6= ['P..TSCSP.W']
#domain6= ['FG..GGV','FC..GGV']
#domain10= 'AA.RT'
domain7= ['E.MGC..GC..G.G','E.MAC..GC..G.G','E.MTC..GC..G.G','E.MCC..GC..G.G','E.MSC..GC..G.G']

#构建二维数组
domain=[domain1,  domain2,  domain3,  domain4, domain5, domain6, domain7]

#打开fasta文件
file_object = open(fasta_file)
try:
        all_the_fasta = file_object.read( )
finally:
        file_object.close()

#使用“>”将fasta文件分成单个序列
fastas = all_the_fasta.split('>')

#遍历各个序列
for fasta in fastas:
#    print fasta
#在循环遍历domain之前设置i变量，针对每个fasta序列都使i=0
    i = 0
    # found=0   #如果想只输出找到目的domain的序列，则在此设置一个值found,初始为0，如果找到则为1，如果为1，则输出，否则，continue
#设置空字符串name，针对每个fasta序列都使name为空
    name=""
#遍历二维数组domain
    for dom in domain:
#每循环一个dom，则i加1
        i = i + 1
#遍历dom中的各个元素
        for element in dom:
#在fasta文件中寻找元素
            f = re.findall(element,fasta)
            if len(f) > 0:
                # found=1
#如果找到，则使名字的字符串加上所找到的元素所在的dom的名字
                name = name + 'domain'  + str(i) + '_'
# if found== 1:
#当针对一个fasta序列的循环结束后，将已经把名字改掉的序列输出
    print '>' + name + fasta
