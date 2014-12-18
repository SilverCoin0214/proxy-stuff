## -----------------------------------
##    Zero's single proxy checker
## -----------------------------------

import os

ip = raw_input('Enter proxy:\n')

hostname = '%s' %ip
answer = os.system("ping -c 1 " + hostname + ">nul")

if answer == 0:
  print ip, '+'
else:
  print ip, '-'
