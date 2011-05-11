import cv
import json
import glob
import os
import sys
import matplotlib.pyplot as plt

mat 	= lambda x: cv.CreateMat(x.rows, x.cols, cv.CV_32FC1)
unzip = lambda l: [[x for x,y in l],[y for x,y in l]]

filesets = ["a","k","m"]

c = ['r','g','b']
s = ['^','o','s']

def plotify(features):
	global c,s
	for u in range(len(features)):
		user = features[u]
		print len(features)
		for i in range(len(user)):
				img = user[i]
				plt.plot(img[0], img[1], c[u]+s[u])

if __name__ == "__main__":
  print 
  imagesets = [
  	[ cv.LoadImageM(fnames, cv.CV_LOAD_IMAGE_GRAYSCALE)
  		for fnames in glob.glob(  os.path.join(( len(sys.argv) > 1 
                                              and sys.argv[1]) or '.',
                                fprefix+'*.jpg')
        ) ]
  			for fprefix in filesets ]
  
  imagesets = [ 
    [ (img,mat(img)) for img in images ]
       for images in imagesets ]
  
  features = [ [
  		#unzip(cv.GoodFeaturesToTrack( img, img_m, img_m, 
      #                              100, 0.04, 50.0,
      #                              blockSize=7))
      unzip([x[0] for x in cv.HoughLines2(img, cv.CreateMemStorage(), 1, 1, 1, 1, 0)])
  		for img,img_m in images ] 
  			for images in imagesets ]
  
  with open('features.json', 'w') as file:
    file.write(json.dumps(features))

  plotify(features)
  plt.savefig('results.png')
  
  # Matplotlib via ports sucks on OS X, so we can't plot :-/
  #plt.plot()
  os.system('open results.png')
  
