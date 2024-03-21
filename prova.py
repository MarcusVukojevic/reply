from utils import * 
from Tiles import Tile

lista_files = ["00-trailer", "01-comedy", "02-sentimental", "03-adventure", "04-drama", "05-horror"]
for nome_input in lista_files:
    #nome_input = "00-trailer"
    griglia, diz_golden, diz_silver, diz_tiles = carica_dataset(f"{nome_input}.txt")

    '''
    lista_tiles = {
        "3" : Tile("3", [[[(1,0), (1,0)], [(-1,0), (-1, 0)]]]),
        "5" : Tile("5", [[[(-1,0), (0,-1)], [(0,1), (1,0)]]]),
        "7" : Tile("7", [[[(1,0), (1, 0)], [(-1,0), (-1, 0)]],[[(-1,0), (0,-1)], [(0,1), (1,0)]], [[(1,0), (0,1)], [(0,-1), (-1, 0)]]]),
        "6" : Tile("6", [[[(1,0), (0,1)], [(0,-1), (-1, 0)]]]),
        "9" : Tile("9", [[[(0,1), (1,0)], [(-1, 0), (0, -1)]]]),
        "96" : Tile("96", [[[(1,0), (0,1)], [(0,-1), (-1, 0)]], [[(0,1), (1,0)], [(-1, 0), (0, -1)]]]),
        "A" : Tile("A", [[[(0,1), (-1,0)], [(1,0), (0, -1)]]]),
        "A5" : Tile("A5", [[[(0,1), (-1,0)], [(1,0), (0, -1)]], [[(-1,0), (0,-1)], [(0,1), (1,0)]]]),
        "B" : Tile("B", [[[(0,1), (-1,0)], [(1,0), (0, 1)]], [[(1,0), (1, 0)], [(-1,0), (-1, 0)]], [[(0,1), (1,0)], [(-1, 0), (0, -1)]]]),
        "C" : Tile("C", [[[(0, -1), (0, -1)], [(0,1), (0,1)]]]),
        "C3" : Tile("C3", [[[(0, -1), (0, -1)], [(0,1), (0,1)]], [[(1,0), (1, 0)], [(-1,0), (-1, 0)]]]),
        "D" : Tile("D", [[[(0, -1), (0, -1)], [(0,1), (0,1)]], [[(0,1), (1,0)], [(-1, 0), (0, -1)]], [[(-1,0), (0,-1)], [(0,1), (1,0)]]]),
        "E" : Tile("E", [[[(0, -1), (0, -1)], [(0,1), (0,1)]], [[(0,1), (-1,0)], [(1,0), (0, -1)]], [[(1,0), (0,1)], [(0,-1), (-1, 0)]]]),
        "F" : Tile("E", [[[(1,0), (1, 0)], [(-1,0), (-1, 0)]], [[(0, -1), (0, -1)], [(0,1), (0,1)]], [[(-1,0), (0,-1)], [(0,1), (1,0)]], [[(1,0), (0,1)], [(0,-1), (-1, 0)]], [[(0,1), (1,0)], [(-1, 0), (0, -1)]], [[(0,1), (-1,0)], [(1,0), (0, -1)]]]),
    }
    '''

    lista_tiles = {
        "3" : Tile("3", [("E", "O"), ("O", "E")]),
        "5" : Tile("5", [("S", "E"), ("E", "S")]),
        "7" : Tile("7", [("E", "S"), ("E", "O"), ("S", "O"), ("S", "E"), ("O", "E"), ("O", "S")]),
        "6" : Tile("6", [("O", "S"), ("S", "O")]),
        "9" : Tile("9", [("N", "E"), ("E", "N")]),
        #"96" : Tile("96", [("N", "O"), ("O", "N"),("E", "S"), ("S", "E")]),
        "A" : Tile("A", [("O", "N"), ("N", "O")]),
        "B" : Tile("B", [("E", "N"), ("N", "E"), ("N", "O"), ("O", "N"),("E", "O"), ("O", "E")]),
        "C" : Tile("C", [("N", "S"), ("S", "N")]),
        #"C3" : Tile("C", [("N", "S"), ("S", "N")]),
        "D" : Tile("D", [("N", "S"), ("S", "N"), ("N", "E"), ("E", "N"), ("S", "E"), ("E", "S")]),
        "E" : Tile("E", [("N", "S"), ("S", "N"),("O", "N"), ("N", "O"), ("O", "S"), ("S", "O")]),
        "F" : Tile("F", [("N", "S"), ("S", "N"),("E", "N"), ("N", "E"), ("E", "S"), ("S", "E"), ("E", "O"), ("O", "E"), ("N", "O"), ("O", "N"), ("S", "O"), ("O", "S")]),

    }

    fatte = []
    lista_paths_finale = []
    for chiave1 in diz_golden:
        for chiave2 in diz_golden:
            if chiave1 == chiave2:
                continue
            else:
                if chiave2 in fatte:
                    continue
                else:
                    lista_path, costo_path = manhattan_path(diz_golden[chiave1], diz_golden[chiave2])

                    corrente = lista_path[0]
                    costo_path = 0 
                    path = []
                    path_finali = []
                    for i in range(len(lista_path)):
                        if i == 0:
                            continue
                        else:
                            direzione = (corrente[0] - lista_path[i][0],  corrente[1] - lista_path[i][1])
                            direzione_scelta = get_direzione(direzione)
                            lista_tiles_scelti = get_tiles(direzione_scelta, lista_tiles)
                            #print(lista_tiles_scelti)
                            corrente = lista_path[i]
                            tile_scelta, diz_tiles = scegli_tile(lista_tiles_scelti, diz_tiles)
                            costo_path = costo_path + diz_tiles[tile_scelta][0]
                            if i != len(lista_path) - 1:
                                path_finali.append(lista_path[i])
                                path.append(tile_scelta)
                    risultati = list(zip(path, path_finali))
                    lista_paths_finale.append(risultati)
        fatte.append(chiave1)

    print(lista_paths_finale)

    with open(f"output/{nome_input}_out.txt", "w") as f:
        for i in lista_paths_finale:
            for j in i:
                f.write(str(j[0]) + " " + str(j[1][0]) + " " + str(j[1][1]) + "\n")
            
