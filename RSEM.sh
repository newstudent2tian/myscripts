#!/bin/sh
#PBS -N RSEM_pi_t
#PBS -o /leofs/cell_lab/yangby/rs_tr/RSEM_tian/pi/RSEM_pi_stdout.txt
#PBS -e /leofs/cell_lab/yangby/rs_tr/RSEM_tian/pi/RSEM_pi_stderr.txt
#PBS -q bioque

export PATH=$PATH:/leofs/cell_lab/yangby/rsem-1.2.8

cd /leofs/cell_lab/yangby/rs_tr/RSEM_tian/pi

perl /leofs/cell_lab/yangby/rs_tr/RSEM/run_RSEM_align_n_estimate.pl --transcripts /leofs/cell_lab/yangby/rs_tr/RSEM_tian/pi/Trinity_1203.fasta --seqType fq --left /leofs/cell_lab/yangby/rs_tr/RSEM_tian/pi/pi3_5_1.fastq.trimmed.paired1 --right /leofs/cell_lab/yangby/rs_tr/RSEM_tian/pi/pi3_5_1.fastq.trimmed.paired2 --SS_lib_type FR --prefix pi --thread_count 10 --no_group_by_component
