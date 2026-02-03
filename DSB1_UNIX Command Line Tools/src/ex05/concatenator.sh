#!/bin/sh

pivot_file='../ex03/hh_positions.csv'
output_file='concatenated.csv'

# список всех .csv-файлов в директории
files=$(ls *.csv | grep -v "${output_file}$")

# берем заголовки из первого
first_file=$(echo "$files" | head -n 1)
head -n 1 "$first_file" > "$output_file"

for file in $files; do
    tail -n +2 "$file" >> "$output_file"
done

if cmp -s  $pivot_file $output_file; then
    echo "Файлы ПОЛНОСТЬЮ ИДЕНТИЧНЫ"
else
    echo "Файлы РАЗЛИЧАЮТСЯ"
fi