import os
import numpy as np

def create_input(width, height, step=1):
    with open('input.txt', 'w') as input:
        for i in np.arange(-width, width, step):
            for j in np.arange(-height, height, step):
                input.writelines(f'{i} {j} \n')
    return