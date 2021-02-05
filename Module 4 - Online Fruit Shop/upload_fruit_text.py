#!/usr/bin/env python3


def process_files(directory):
  """Given a directory, take each text file and add their contents to
  a dictionary in a list. Return the list of dictionaries.
  """


def upload_descriptions(descriptions):
  """Given a list of dictionaries, upload it as a JSON object with a
  POST request.
  """


def main(argv):
  # Process each text file and add to a list of dictionaries
  descriptions = process_files(directory)
  # Upload list of dictionaries as a JSON
  upload_descriptions(descriptions)

if __name__ == "__main__":
  main(sys.argv)
