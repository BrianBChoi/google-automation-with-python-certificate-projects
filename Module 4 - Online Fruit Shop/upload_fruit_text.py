#!/usr/bin/env python3


import os
import requests


def process_files(files):
  """Given a list of files, take each text file and add their contents to
  a dictionary in a list. Return the list of dictionaries.
  """


def upload_descriptions(descriptions):
  """Given a list of dictionaries, upload it as a JSON object with a
  POST request.
  """
  response = requests.post(
    "http://<REPLACE_WITH_IP>/fruits/", json=descriptions)
  response.raise_for_status()


def main(argv):
  directory = argv[1]
  files = os.listdir(directory)
  descriptions = process_files(files)
  upload_descriptions(descriptions)

if __name__ == "__main__":
  main(sys.argv)
