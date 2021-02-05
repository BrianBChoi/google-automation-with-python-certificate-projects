#!/usr/bin/env python3


import os, sys
from upload_fruit_text import process_files
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def report_text(descriptions):
  """Isolates the name and weight of each fruit and returns a string that will
  compose the body of the PDF.
  """
  report = ""
  for fruit in descriptions:
    report += "name: {}<br/>".format(fruit["name"])
    report += "weight: {} lbs<br/><br/>".format(fruit["weight"])
  return report


def generate(filename, title, body_text):
  """Given a filename, a title, and the content of the report, generates and
  saves a PDF file."""
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(body_text, styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line, report_table])


def main(argv):
  """Generates a PDF report of the uploaded fruits that includes the name and
  weight of each fruit.
  """
  directory = argv[1]
  files = os.listdir(directory)
  os.chdir(directory)
  descriptions = process_files(files)

  report = report_text(descriptions)
  date = datetime.today().strftime('%Y-%m-%d')
  title = "Processed Update on {}".format(date)
  generate("/tmp/processed.pdf", title, report)

if __name__ == "__main__":
  main(sys.argv)
