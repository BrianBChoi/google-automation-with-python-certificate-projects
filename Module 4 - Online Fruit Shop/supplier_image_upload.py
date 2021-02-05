#!/usr/bin/env python3

import os
import requests


def main(argv):
  """Upload all the files in a given directory to
  http://localhost/upload/
  """
  image_dir = argv[1]
  files = os.listdir(image_dir)
  os.chdir(image_dir)

  for image in files:
    with open(image, 'rb') as opened:
      r = requests.post('http://localhost/upload/', files={'file': opened})


if __name__ == "__main__":
  main(sys.argv)
