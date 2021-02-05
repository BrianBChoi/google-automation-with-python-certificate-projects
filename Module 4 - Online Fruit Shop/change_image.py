#!/usr/bin/env python3

from PIL import Image
import os, sys


def get_images(directory, ext):
  """Given a directory of images and the desired extension, returns a
  list of the images with matching extensions"""
  files = os.listdir(directory)
  images = []
  for file in files:
    if file.endswith(ext):
      images.append(file)
  return images


def process_images(images):
  """Given a list of image file names, changes their size to 600x400 and
  saves each as a JPEG
  """
  for file in images:
    image = Image.open(file)
    new_image = image.resize((600, 400)).convert('RGB')
    filename = os.path.splitext(file)[0] + '.jpeg'
    new_image.save(filename)


def main(argv):
  image_dir = argv[1]
  images = get_images(image_dir)
  os.chdir(image_dir)
  process_images(images)


if __name__ == "__main__":
  main(sys.argv)
