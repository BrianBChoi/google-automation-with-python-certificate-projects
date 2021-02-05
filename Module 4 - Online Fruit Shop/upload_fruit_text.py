#!/usr/bin/env python3


import os, sys
import requests


def process_files(files):
  """Given a list of files, take each text file and add their contents to
  a dictionary in a list. Return the list of dictionaries.
  """
  descriptions = []
  for file in files:
    with open(file) as text:
      description = {}
      for positon, line in enumerate(text):
        if position == 0:
          description["name"] = line.strip("\n")
        if position == 1:
          description["weight"] = line.strip(" lbs\n")
        if position == 2:
          description["description"] = line.strip("\n")
    image_name = os.path.splitext(file)[0] + ".jpeg"
    description["image_name"] = image_name
    descriptions.append(description)

  return descriptions

def upload_descriptions(descriptions):
  """Given a list of dictionaries, upload it as a JSON object with a
  POST request.
  """
  for description in descriptions:
    response = requests.post(
      "http://<REPLACE_WITH_IP>/fruits/", json=description)
    response.raise_for_status()


def main(argv):
  directory = argv[1]
  files = os.listdir(directory)
  os.chdir(directory)
  descriptions = process_files(files)
  upload_descriptions(descriptions)

if __name__ == "__main__":
  main(sys.argv)
