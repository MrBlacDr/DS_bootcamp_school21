#!/bin/sh

input_file='../ex03/hh_positions.csv'
output_file='hh_uniq_positions.csv'

awk -v OFS=',' '
BEGIN {print "\"name\"","\"count\""}' > $output_file;

awk -F',' '
NR>1 && $3 != "\"-\"" {count[$3]++} END {
    for (level in count) printf "%s,%d\n", level, count[level]
}' $input_file | sort >> $output_file