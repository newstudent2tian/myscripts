#!/bin/sh
#PBS  -N Trin_sc
#PBS -o /leofs/cell_lab/bigyangby/rs_tr/trinity/pixin/screened/screen_stdout.txt
#PBS -e /leofs/cell_lab/bigyangby/rs_tr/trinity/pixin/screened/screen_stderr.txt
#PBS -l nodes=fat08     
#PBS -q asmque          

cd /leofs/cell_lab/bigyangby/rs_tr/trinity/pixin/screened/read_pinxin_result

export LD_LIBRARY_PATH=/software/biosoft/software/curl7.28.1/lib:/software/gcc471/gcc-4.7.1/lib64:/software/gcc471/gmp-5.0.4/lib:/software/gcc471/mpc-0.8.1/lib:/software/gcc471/mpfr-2.4.2/lib:$LD_LIBRARY_PATH

Trinity.pl --seqType fq --JM 60G --left /leofs/cell_lab/bigyangby/rs_tr/trinity/pixin/screened/read_pinxin_result/reads.pixin.1.fq.paired1 --right /leofs/cell_lab/bigyangby/rs_tr/trinity/pixin/screened/read_pinxin_result/reads.pixin.1.fq.paired2 --SS_lib_type FR --CPU 8 
