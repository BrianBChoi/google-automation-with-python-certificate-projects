#! /usr/bin/env python3

import os
import requests

def process_file(file):
    review = {}
    # open file and process review
    return review

def upload_file(review):
    response = requests.post('http://<REPLACE WITH IP>/feedback', json=review)
    response.raise_for_status()

if __name__ == '__main__':
    for files in os.listdir('data/feedback'):
        review = process_file(file)
        upload_file(review)
