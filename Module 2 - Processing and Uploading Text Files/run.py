#! /usr/bin/env python3

import os
import requests

def processFile(file):
    review = {}
    # open file and process review
    return review

def uploadFile(review):
    response = requests.post('http://<REPLACE WITH IP>/feedback', json=review)
    response.raise_for_status()

if __name__ == '__main__':
    for files in os.listdir('data/feedback'):
        review = processFile(file)
        uploadFile(review)
