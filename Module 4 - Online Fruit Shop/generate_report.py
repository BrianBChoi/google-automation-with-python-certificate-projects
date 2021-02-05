#!/usr/bin/env python3


import os
from upload_fruit_text import process_files


def main(argv):
  # use process_files from upload_fruit_text.py to get all fruit descriptions
  directory = argv[1]
  files = os.listdir(directory)
  os.chdir(directory)
  descriptions = process_files(files)
  
  # create report body text with fruit descriptions
  # get date
  # generate report and save

if __name__ == "__main__":
  main(sys.argv)
