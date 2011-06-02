import glob
import os
import sys

finder = lambda x: glob.glob(os.path.join(sys.argv[1], x))
files  = finder('*.jpg') + finder('*.JPG')

assert(sys.argv[2] in ['a', 'k', 'm'])
assert all(map( lambda x: not x ,
         [os.system( 'mv ' + x.replace(' ', '\ ') + ' ' 
                      + os.path.join(sys.argv[1], sys.argv[2] 
                      + str(y) + '.jpg' ))
            for x, y in zip(files, range(len(files)))]
        ))


