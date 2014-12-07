#! /usr/bin/perl;
use Bio::Seq;
use Bio::SeqIO;
use List::MoreUtils qw(uniq);

################### usage ##################################
# perl tiqu_2013.pl list database
# the output file will be list.fasta
#######################################################

########## BIGIN: Cofiguration ##########################################################
$file2Find=$ARGV[0];
$file2BeFound=$ARGV[1];
########## END: Configuration ###########################################################

########## BIGIN: processing seq by seq #################################################
$i=0;
open(FILE,$file2Find);
open(OUT,">$file2Find.fasta");
@list2find=<FILE>;
@list2find = uniq @list2find;
$total=@list2find;
my $seq_obj;
my @seq_obj_array;

my $seqio_obj = Bio::SeqIO->new(-file => $file2BeFound, -format => "fasta" ); #create a seqIO obj to read a seqfile.
while ($seq_obj = $seqio_obj->next_seq){ #to read each seq in the seqfile.
push(@seq_obj_array,$seq_obj);
}
#@seq_obj_array = uniq @seq_obj_array;

foreach $query_id (@list2find){
  $i++;
  chomp($query_id);
  print "$i/$total\t$query_id";
  if($query_id eq ""){
  print " empty\n";
  next;
  }
  $ctrl=0;
  foreach $seq_i (@seq_obj_array){
    $seqname=$seq_i->display_id; #to get the id of the read seq.
    if($seqname =~ m/$query_id/) {
      $seqstr=$seq_i->seq();
      print OUT ">$seqname\n$seqstr\n";
      print " is found;\n";
      $ctrl=1;
      last;    
    }  
  }
  if($ctrl==0){
    print ">The $query_id is not found. Please take attension to this sequence ID.\n\n";
    print " is not found;\n";
  }
  
}

close(FILE);
close(OUT);

########## END: processing seq by seq #################################################################
