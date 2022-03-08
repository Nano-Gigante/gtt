from gtt import gtt
import os

g = gtt()

#train for every topic
traindir = "dataset"
for file in os.listdir(traindir):
    p = traindir + '/' + file
    print(f'train: {p}')
    g.train(p)

idir = "inputs"
for file in os.listdir(idir):
    p = idir + '/' + file
    print(f'\ngtt: {p}')

    print("\t"+g.guess_the_topic(p))
