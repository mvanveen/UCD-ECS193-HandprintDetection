import pickle
import sys

import milk

assert(sys.argv[1])
features = pickle.load(open(sys.argv[1], 'r'))
trainer  = milk.defaultlearner()

model = trainer.train(*features)

pickle.dump(model, open('trainer.pik', 'w'))
