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
  file_name = sys.argv[1]

  print('starting')
  prev = determineID(file_name)
  time.sleep(10)
  current = determineID(file_name)
  print('finishing')

  if current != prev:
    print('something has changed')


# TODO
# add modification history