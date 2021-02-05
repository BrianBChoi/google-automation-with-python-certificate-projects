#!/usr/bin/env python3


import os
from upload_fruit_text import process_files
from datetime import datetime

def report_text(descriptions):
  report = ""
  for fruit in descriptions:
    report += "name: {}<br/>".format(fruit["name"])
    report += "weight: {} lbs<br/><br/>".format(fruit["weight"])
  return report


def main(argv):
  # use process_files from upload_fruit_text.py to get all fruit descriptions
  directory = argv[1]
  files = os.listdir(directory)
  os.chdir(directory)
  descriptions = process_files(files)

  # create report body text with fruit descriptions
  report = report_text(descriptions)

  # get date
  date = datetime.today().strftime('%Y-%m-%d')
  
  # generate report and save

if __name__ == "__main__":
  main(sys.argv)
