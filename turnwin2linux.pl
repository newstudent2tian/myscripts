#!/usr/bin/perl

open (F,$ARGV[0]);
open (O,">$ARGV[1]");

while (<F>)
{
s/\r//;

print O $_;
}
