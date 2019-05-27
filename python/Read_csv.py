# 1. string split
with open('lunch.csv','r',encoding='utf-8') as f:
    lines=f.readlines()
    for line in lines:
        print(line.strip().split(',')) # strip 은 개행문자를 없에준다.

# 2. csv
import csv
with open('lunch.csv','r',encoding='utf-8') as f:
    items=csv.reader(f.readlines())
    for item in items:
        print(item)