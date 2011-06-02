import os
import time

get_progress = lambda x: 1. - (x - int(os.popen('wc -l results.log').read().lstrip().split(' ')[0])) / float(x)

while(True):
  os.system('clear')
  print "Percent finished: " + str(get_progress(482)*100.) + '%...'
  time.sleep(1)
