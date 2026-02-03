#!/bin/sh

input_file="../ex03/hh_positions.csv"

awk -F',' '
NR == 1 {
    header = $0  # сохранить заголовки
    next
}
{
    date = $2
    
    # Создаем файл и записываем заголовки
    if (!(date in files)) {
        printf "%s\n", header > (date ".csv")
        files[date] = 1
    }
    
    # Добавляем текущую строку в созданный файл
    print >> (date ".csv")
}' "$input_file"
