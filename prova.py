from utils import * 

griglia, diz_golden, diz_silver, diz_tail = carica_dataset("00-trailer.txt")

print(diz_golden['G1'],diz_golden['G2'])


print(manhattan_path(diz_golden['G1'],diz_golden['G2']))