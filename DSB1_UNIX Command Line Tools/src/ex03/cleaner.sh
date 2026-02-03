#!/bin/sh

input_file="../ex02/hh_sorted.csv"
output_file="hh_positions.csv"

# Обрабатываем CSV
awk -F',' -v OFS=',' ' # считываем по запятым и в итоговый файл передаем так же
NR == 1 { print; next } # первая строка
{
  # Извлекаем уровень из названия
  level = "-"
  if ($3 ~ /Junior/) level = "Junior"
  if ($3 ~ /Middle/) level = (level == "-" ? "Middle" : level "/Middle")
  if ($3 ~ /Senior/) level = (level == "-" ? "Senior" : level "/Senior")
  
  # Формируем новую строку
  print $1, $2, "\"" level "\"", $4, $5
}' "$input_file" > "$output_file"
