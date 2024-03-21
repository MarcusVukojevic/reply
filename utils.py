def manhattan_path(p1, p2):
    # Estrazione delle coordinate dei punti
    x1, y1 = p1
    x2, y2 = p2
    
    # Lista per mantenere il percorso
    path = []
    
    # Aggiunta del punto di partenza al percorso
    path.append((x1, y1))
    
    # Movimento orizzontale da x1 a x2
    step = 1 if x1 < x2 else -1
    for x in range(x1 + step, x2 + step, step):
        path.append((x, y1))
    
    # Movimento verticale da y1 a y2
    step = 1 if y1 < y2 else -1
    for y in range(y1 + step, y2 + step, step):
        path.append((x2, y))
    
    return path, abs(x2-x1) + abs(y2-y1)


def carica_dataset(nome_file):
    with open(f'input_files/{nome_file}', 'r') as file:
    # Leggo l'intero contenuto del file
        lines = file.readlines()

    i = 0 
    griglia = []
    diz_golden = {}
    diz_silver = {}
    diz_tail = {}
    for line in lines:
        line = line.strip('\n').strip('ï»¿').split()
        if i == 0 :
            griglia = [line[0], line[1]]
            num_golden = int(line[2])
            num_silver = int(line[3])
            num_tail = int(line[4])
        elif i <= num_golden:
            diz_golden[f'G{i}'] =  [int(z) for z in line]
        elif i <= num_golden + num_silver:
            diz_silver[f'G{i- num_golden}'] =  [int(z) for z in line]
        elif i <= num_golden + num_silver + num_tail:
            diz_tail[line[0]] = [int(line[1]), int(line[2])]
        i = i+1

    return griglia, diz_golden, diz_silver, diz_tail

def get_direzione(tupla):
    if tupla[0] == -1 and tupla[1] == 0:
        return ("O", "E")
    elif tupla[0] == 1 and tupla[1] == 0:
        return ("E", "O")
    elif tupla[0] == 0 and tupla[1] == 1:
        return ("S", "N")
    elif tupla[0] == 0 and tupla[1] == -1:
        return ("N", "S")
    elif tupla[0] == -1 and tupla[1] == -1:
        return ("S", "E")
    elif tupla[0] == -1 and tupla[1] == 1:
        return ("N", "E")
    elif tupla[0] == 1 and tupla[1] == 1:
        return ("N", "O")
    elif tupla[0] == 1 and tupla[1] == -1:
        return ("S", "O")




def get_tiles(direzione, lista_tiles):
    tiles_ritorno = []
    for i in lista_tiles:
        if(direzione in lista_tiles[i].lista_arrivi):
            tiles_ritorno.append(i)

    return tiles_ritorno


def scegli_tile(lista_tiles_scelti, diz_tiles):
    #print(lista_tiles_scelti)
    min = 1000000
    for chiave in lista_tiles_scelti:
        costo = diz_tiles[chiave][0]
        if costo<min:
            min = costo
            num_min = diz_tiles[chiave][1] 
            chiave_min = chiave
    diz_tiles[chiave_min][1] = num_min-1
    return chiave_min, diz_tiles



    
