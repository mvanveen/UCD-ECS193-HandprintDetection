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
  for u in r)ange(len(features)):
		user = features[u]
		for i in reversed(range(len(user))):
				img = user[i]
				plt.plot(img[0], img[1], c[u]+s[u])

if __name__ == "__main__":
  imagesets = [
  	[ cv.LoadImageM(fnames, cv.CV_LOAD_IMAGE_COLOR)
  		for fnames in glob.glob(  os.path.join(( len(sys.argv) > 1 
                                              and sys.argv[1]) or '.',
                                fprefix+'*.jpg')
        ) ]
  			for fprefix in filesets ]

  print imagesets
  img1  = cv.LoadImage('set2/m2.jpg', cv.CV_LOAD_IMAGE_COLOR)
  grey  = cv.CreateImage(cv.GetSize(img1), cv.IPL_DEPTH_8U, 1) 

  features = [[], [], []]
  for images, i in zip(imagesets, range(len(imagesets))):
    for img in images:
      cv.CvtColor(img, grey, cv.CV_RGB2GRAY)
      try:
          features[i].append(cv.ExtractSURF(grey, None, cv.CreateMemStorage(), (0, 3000, 3, 4))[0][0][0])
      except Exception, e:
        print e
  print features 
  with open('features_surf.json', 'w') as file:
    file.write(json.dumps(features))

  plotify(features)
  plt.savefig('results.png')
  
  # Matplotlib via ports sucks on OS X, so we can't plot :-/
  #plt.plot()
  os.system('open results.png')
  
