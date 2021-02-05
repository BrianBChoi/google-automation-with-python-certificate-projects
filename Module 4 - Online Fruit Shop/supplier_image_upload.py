#!/usr/bin/env python3

import os, sys
import requests
from change_image import get_images


def main(argv):
  """Upload all JPEG images in a given directory to
  http://localhost/upload/
  """
  image_dir = argv[1]
  images = get_images(image_dir, ".jpeg")
  os.chdir(image_dir)

  for image in images:
    with open(image, 'rb') as opened:
      r = requests.post('http://localhost/upload/', files={'file': opened})


if __name__ == "__main__":
  main(sys.argv)
