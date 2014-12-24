#!/usr/bin/perl
#Informatic Biology departments of Beijing Genomics Institute (BGI) 
use strict;
use Getopt::Long;
#use Smart::Comments '###';
my %opts;
my $program=`basename $0`;
chomp $program;
my $usage=<<USAGE; #******* Instruction of this program *********#

#example:perl fish_pri.pl -tbait list -tfish fa(文件格式) -contrary（若与id中序列相同，要去掉。若要调出除id以外的序列，则加这一参数）id（序列名字集合，来自源文件，用grep取出） longer_than_150_line.fasta（想要调出序列的原文件）
#usage: perl fish_pri.pl -tbait list -tfish fa -contrary id .fasta >.fasta
#取得id后要将每行首的“”去掉，命令为:%s/^>//g

Author:  Fan wei, <fanw\@genomics.org.cn>, new year 2006

Program: fishing in one file according to bait in another file

Usage: $program  <bait_file fish_file>
    -tbait<type>		type of bait file
	-tfish<type>		type of fish file
	-bait <colum>       colum as bait
	-fish <colum>       colum as fish
	-contrary			fish those not in the bait
	-details            output the middle results to screen
	-help               output help information

Comment: This is a frequently used program, which deals with the most frequetly used 
file format .fa, .psl, and .list(just like excel tables which have several colums and rows).
It gets the baits(key that is universal in both bait and fish file) from the bait file
at first, and then searches the baits in the fish file. If found, then retrive that item
from the fish file. If -contrary is specifed, retrive those items which are not exist
in the bait file.

USAGE

GetOptions(\%opts, "bait:i","fish:i","tbait:s","tfish:s","details!","contrary","help!");
die $usage if ( @ARGV==0 || defined($opts{"help"}));

#****************************************************************#
#--------------------Main-----Function-----Start-----------------#
#****************************************************************#
my $bait_file=shift;
my $fish_file=shift;
my %bait;


if ( $opts{tbait} eq 'psl'  || ( ! exists $opts{tbait} && $bait_file=~/.psl$/ ) ) {
	read_psl($bait_file,\%bait);
}elsif($opts{tbait} eq 'fa' || ( ! exists $opts{tbait} && $bait_file=~/.fa$/ ) ){
	read_fa($bait_file,\%bait);
}else{
	read_list($bait_file,\%bait);
}

print STDERR "read bait done\n" if (exists $opts{details});

if ($opts{tfish} eq 'psl' || ( ! exists $opts{tfish} && $fish_file=~/.psl$/ ) ) {
	out_psl($fish_file,\%bait);
}elsif($opts{tfish} eq 'fa' || ( ! exists $opts{tfish} && $fish_file=~/.fa$/ ) ){
	out_fa($fish_file,\%bait);
}else{
	out_list($fish_file,\%bait);
}

print STDERR "Fish out done\n" if (exists $opts{details});
#****************************************************************#
#------------------Children-----Functions-----Start--------------#
#****************************************************************#

sub read_list{
	my $file=shift;
	my $bait_hp=shift;
	my $bait_colum=($opts{bait}) ? $opts{bait} : 1;
	open(IN,$file)||die("fail to open $file\n");
	while (<IN>) {
		my @temp=split(/\s+/,$_);
		$$bait_hp{$temp[$bait_colum-1]}=1;
		#print "bait:$temp[$bait_colum-1]\n";

	}
	close(IN);
}

sub read_psl{
	my $file=shift;
	my $bait_hp=shift;
	my $bait_colum=($opts{bait}) ? $opts{bait} : 10;
	open(IN,$file)||die("fail to open $file\n");
	while (<IN>) {
		my @temp=split(/\s+/,$_);
		$$bait_hp{$temp[$bait_colum-1]}=1;
	}
	close(IN);
}

sub read_fa{
	my $file=shift;
	my $bait_hp=shift;
	my $bait_colum=($opts{bait}) ? $opts{bait} : 1;
	open(IN,$file)||die("fail to open $file\n");
	$/=">";<IN>;$/="\n";
	while (<IN>) {
		my $title=$_;
		$/=">";
		my $seq=<IN>;
		chomp $seq;
		$/="\n";
		my @temp=split(/\s+/,$title);
		$$bait_hp{$temp[$bait_colum-1]}=1;
	}
	close(IN);
}



sub out_list{
	
	my $file=shift;
	my $fish_hp=shift;
	my $fish_colum=($opts{fish}) ? $opts{fish} : 1;
	
	my $output;
	open(IN,$file)||die("fail to open $file\n");
	while (<IN>) {
chomp;		
my @temp=split(/\s+/,$_);
		$output .= $_."\t".$$fish_hp{$temp[$fish_colum-1]}."\n" if ( exists $$fish_hp{$temp[$fish_colum-1]} && !exists $opts{contrary});
		$output .= $_ if ( !exists $$fish_hp{$temp[$fish_colum-1]} && exists $opts{contrary});
	}
	close(IN);
	print $output;
}

sub out_psl{
	my $file=shift;
	my $fish_hp=shift;
	my $fish_colum=($opts{fish}) ? $opts{fish} : 10;
	my $output;
	open(IN,$file)||die("fail to open $file\n");
	while (<IN>) {
		my @temp=split(/\s+/,$_);
		$output .= $_ if ( exists $$fish_hp{$temp[$fish_colum-1]} && !exists $opts{contrary});
		$output .= $_ if ( !exists $$fish_hp{$temp[$fish_colum-1]} && exists $opts{contrary});
	}
	close(IN);
	print $output;
}

sub out_fa{
	my $file=shift;
	my $fish_hp=shift;
	my $fish_colum=($opts{fish}) ? $opts{fish} : 1;
	my $output;
	open(IN,$file)||die("fail to open $file\n");
	$/=">";<IN>;$/="\n";
	while (<IN>) {
		my $title=$_;
		$/=">";
		my $seq=<IN>;
		chomp $seq;
		$/="\n";
		my @temp=split(/\s+/,$title);
		#$temp[$fish_colum-1]=~s/\.\d//;
		#print "fa:$temp[$fish_colum-1]\n";
		$output .= ">".$title.$seq if ( exists $$fish_hp{$temp[$fish_colum-1]} && !exists $opts{contrary});
		$output .= ">".$title.$seq if ( !exists $$fish_hp{$temp[$fish_colum-1]} && exists $opts{contrary});
	}
	close(IN);
	print $output;
}
