import sys
import argparse
import os
import time
from libs.coord_builder import create_coords
from libs.merge import merge


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', default='10')
    parser.add_argument('--height', default='10')
    parser.add_argument('--step', default='1')
    args = parser.parse_args()

    try:
        width = int(args.width)
        height = int(args.height)
        step = float(args.step)
    except:
        print('Введите числовые значения аргументов')

    create_coords(width, height, step)
    os.system('"C://Study//polter//plst_1.exe"')
    output = merge('input.txt', 'plst_dstr.txt')
    print(output)
    input()
    


    

    
