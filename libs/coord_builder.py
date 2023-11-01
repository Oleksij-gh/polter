import os
import numpy as np

def create_coords(width, height, step=1):
    with open('input.txt', 'w') as input:
        for i in np.arange(-width, width+1, step):
            for j in np.arange(-height, height+1, step):
                input.writelines(f'{i} {j} \n')
    return