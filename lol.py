import cv
import glob
from   itertools        import chain
from   scipy            import compress
from   scipy.cluster.vq import kmeans, whiten, vq

from pprint import pprint

mat    = lambda x: cv.CreateMat(x.rows, x.cols, cv.CV_32FC1)
images = [cv.LoadImageM(x, cv.CV_LOAD_IMAGE_GRAYSCALE) for 
            x in glob.glob('*.jpg')]
mats = [mat(x) for x in images]
print [type(x) for x in mats]

features = [[ (x, y) for x, y in 
                cv.GoodFeaturesToTrack(img,
                                       mat(img),
                                       mat(img),
                                       10,
                                       0.04,
                                       1.0)] for
                img in images]
features = [x for x in chain(*features)]

wh_data              = whiten(features)
code_book,dist       = kmeans(wh_data, 3, 3, 0.4)
code_ids, distortion = vq(wh_data,code_book)
clusters             = []

for i in range(len(code_book)):
  cluster = compress(code_ids == i,features,0)
  clusters.append(cluster)
print clusters

