import glob
from   itertools import chain
import os
import pickle
import sys

import mahotas.surf

read = lambda x: mahotas.imread(x, as_grey=True)
dir  = (len(sys.argv) > 1 and sys.argv[1]) or '.'

filesets  = ["a","k","m"]
imagesets = [
  	[ (fname, fprefix) for fname 
  		in glob.glob(os.path.join(dir, fprefix+'*.jpg')) ] for fprefix
			  in filesets ]

imagesets = [x for x in chain(*imagesets)]
print len(imagesets)

results = [ (mahotas.surf.surf(read(obj[0])), obj[1]) 
              for obj in imagesets]

with open('features_surf.pik', 'w') as file:
  pickle.dump(results, file)

print results
