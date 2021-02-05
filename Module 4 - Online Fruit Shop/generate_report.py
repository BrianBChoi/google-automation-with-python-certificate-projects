#!/usr/bin/env python3


import os
from upload_fruit_text import process_files
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def report_text(descriptions):
  report = ""
  for fruit in descriptions:
    report += "name: {}<br/>".format(fruit["name"])
    report += "weight: {} lbs<br/><br/>".format(fruit["weight"])
  return report


def generate(filename, title, body_text):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line, report_table])


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
  title = "Processed Update on {}".format(date)

  # generate report and save
  generate("/tmp/processed.pdf", title, report)

if __name__ == "__main__":
  main(sys.argv)
