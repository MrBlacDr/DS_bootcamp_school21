#!/bin/sh

curl -G "https://api.hh.ru/vacancies?text=data+scientist&page=0&per_page=20" | jq > './hh.json'
