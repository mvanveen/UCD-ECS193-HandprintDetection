import os
from multiprocessing import Pool
import pickle
import sys

import mahotas
import milk

def guess(item):
  print str(item) + ' : ...',
  print(trainer.apply(
             mahotas.features.haralick(
               mahotas.imread(item)).mean(0)
          ))

if __name__ == '__main__':
  with open('trainer.pik', 'r') as trainerFile:
    trainer = pickle.load(trainerFile)
  p = Pool(6) 
  results = p.map(guess , sys.argv[1:])
   
