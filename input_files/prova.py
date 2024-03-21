import pandas as pd


with open('00-trailer.txt', 'r') as file:
    # Leggo l'intero contenuto del file
    lines = file.readlines()

i = 0 
griglia = []
diz_golden = {}
diz_silver = {}
diz_tail = {}
for line in lines:
    line = line.strip('\n').strip('ï»¿').split()
    print(line)
    if i == 0 :
        griglia = [line[0], line[1]]
        num_golden = int(line[2])
        print(num_golden)
        num_silver = int(line[3])
        num_tail = int(line[4])
    elif i <= num_golden:
        diz_golden[f'G{i}'] =  line
    elif i <= num_golden + num_silver:
        print(i)
        diz_silver[f'G{i- num_golden}'] =  line
    elif i <= num_golden + num_silver + num_tail:
        print(i)
        diz_tail[ line[0]] = [line[2], line[1]]
    i = i+1
print('diz_golden: ',diz_golden)
print('diz_silver: ',diz_silver)
print('diz_tail: ',diz_tail)
    