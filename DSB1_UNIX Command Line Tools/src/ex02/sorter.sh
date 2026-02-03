#!/bin/sh

# выводит заголовок csv
cat ../ex01/hh.csv | head -n 1 > hh_sorted.csv;

# выводит все без заголовка и отдает на сортировку
cat ../ex01/hh.csv | tail -n +2 | sort -t',' -k2,2 -k1,1 >> hh_sorted.csv