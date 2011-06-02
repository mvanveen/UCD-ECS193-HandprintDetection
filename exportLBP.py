import datetime
import glob
from   itertools import chain
import logging
from   multiprocessing import Pool
import os
import pickle
import sys

import mahotas.surf

then = datetime.datetime.now()

dirs = sys.argv[1:]
read   = lambda x: mahotas.imread(x)
pixels = lambda shape: shape[0] * shape[1]

dir  = (len(sys.argv) > 1 and sys.argv[1]) or '.'

filesets  = ["a","k","m"]
imagesets = [[[ (fname, fprefix) for fname in  
                 glob.glob(
                  os.path.join( dir,
                                fprefix+'*.jpg')
                ) ] for fprefix in filesets ]
                    for dir in dirs ]

compress = lambda y: [x for x in chain(*y)]
imagesets = compress(compress(imagesets))
print len(imagesets)

def f(obj): 
  img = read(obj[0])
  logging.error( 'Processing ' + str(obj[0]) + '...')
  results = (mahotas.features.lbp(img, 16, pixels(img.shape)), obj[1])
  logging.error(results)
  return(results)

p = Pool(6)
results = p.map(f, imagesets)

features = [feature for feature, _ in results]
labels   = [label for _, label in results]

with open('features_lbp.pik', 'w') as file:
  pickle.dump((features, labels), file)

print results
print str(datetime.datetime.now() - then)
