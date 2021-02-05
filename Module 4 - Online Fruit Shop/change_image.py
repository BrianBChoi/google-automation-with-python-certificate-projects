#!/usr/bin/env python3

from PIL import Image
import os


def get_images(directory):
  """Given a directory of images, returns a list of their names"""
  return os.listdir(directory)


def process_images(images):
  """Given a list of image file names, changes their size to 600x400 and
  saves each as a JPEG
  """
  for file in images:
    image = Image.open(file)
    new_image = image.resize((600, 400)).convert('RGB')
    new_image.save(file, 'JPEG')


def main(argv):
  image_dir = argv[1]
  images = get_images(image_dir)
  os.chdir(image_dir)
  process_images(images)


if __name__ == "__main__":
  main(sys.argv)
