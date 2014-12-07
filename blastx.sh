#!/bin/sh
#PBS -N CE
#PBS -o /leofs/cell_lab/yangby/rs_tr_2/CE.out.txt
#PBS -e /leofs/cell_lab/yangby/rs_tr_2/CE.err.txt
#PBS -q bioque
cd /leofs/cell_lab/yangby/rs_tr_2/

blastx -query /leofs/cell_lab/yangby/rs_tr_2/CE-cha-liu.fa -db /leofs/cell_lab/yangby/rs_tr_2/Trinity_1203.fasta -out /leofs/cell_lab/yangby/rs_tr_2/CE_trinity1203.blast -outfmt "7 qseqid qgi qacc qlen sseqid sallseqid sacc slen evalue qstart qend sstart send qseq sseq bitscore score length" -evalue 1e-5 -num_threads 1


