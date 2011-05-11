import pickle
import sys

import milk
import milk.supervised
import milk.supervised.adaboost
import milk.supervised.multi

assert(sys.argv[1])
features = pickle.load(open(sys.argv[1], 'r'))

weak    = milk.supervised.tree.stump_learner()
learner = milk.supervised.adaboost.boost_learner(weak)
learner = milk.supervised.multi.one_against_one(learner)
model = learner.train(*features)

pickle.dump(model, open('trainer.pik', 'w'))

cmat,names, preds = milk.nfoldcrossvalidation(*features,
                                              classifier=learner,
                                              return_predictions=1)

print cmat
print names
print preds
