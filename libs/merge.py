import os

def merge(coords_name, proba_name):
    out = dict()
    with open(coords_name, 'r') as coords_file:
        coords = coords_file.readlines()
    with open(proba_name, 'r') as proba_file:
        proba = proba_file.readlines()
    
    with open('output.txt', 'w') as output:
        for i in range(len(coords)):
            if float(proba[i]) != 0:
                output.writelines(f'{coords[i][:-2]}: {float(proba[i])}\n' )
                out[coords[i][:-2]] = float(proba[i])

    return out