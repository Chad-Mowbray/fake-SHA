import sys
import time


def determineID(file_name):

  uniqueID = 0
  with open(file_name) as file:
    for line in file:
      for char in line:
        uniqueID += ord(char)

  return uniqueID



while True:
  print('starting')
  prev = determineID(sys.argv[1])
  
  time.sleep(10)

  current = determineID(sys.argv[1])
  print('finishing')

  if current != prev:
    print('something has changed')