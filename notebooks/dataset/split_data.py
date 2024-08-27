import os
import shutil
import random

os.mkdir('subset')
os.mkdir('subset/test')
os.mkdir('subset/train')
os.mkdir('subset/val')
#
global_split = 0.35
#
test_split = 0.3
val_split = 0.2
# Copy files from Data to create test and train subsets
dirs = os.listdir('Data')
for d in dirs:
    os.mkdir(f'subset/test/{d}')
    os.mkdir(f'subset/train/{d}')
    #
    files = os.listdir(f'Data/{d}')
    #
    rand = random.sample(files, int(len(files)*global_split))
    rand_test = rand[:int(len(rand)*test_split)]
    rand_train = rand[int(len(rand)*test_split):]
    #
    for rte in rand_test:
        shutil.copy(f'Data/{d}/{rte}', f'subset/test/{d}/{rte}')
    for rtr in rand_train:
        shutil.copy(f'Data/{d}/{rtr}', f'subset/train/{d}/{rtr}')

# Now actually move pictures from train to create val subset

dirs = os.listdir('subset/train')
for d in dirs:
    os.mkdir(f'subset/val/{d}')
    #
    files = os.listdir(f'subset/train/{d}')
    #
    rand_val = random.sample(files, int(len(files)*val_split))
    #
    for r in rand_val:
        os.rename(f'subset/train/{d}/{r}', f'subset/val/{d}/{r}')
