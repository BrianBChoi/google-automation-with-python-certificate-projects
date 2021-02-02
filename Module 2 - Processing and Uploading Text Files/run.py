#! /usr/bin/env python3

import os
import requests

def process_file(file):
    review = {}
    with open(file) as f:
        lines = f.readlines()
        review['title'] = lines[0]
        review['name'] = lines[1]
        review['date'] = lines[2]
        review['feedback'] = lines[3]
    return review

def upload_file(review):
    response = requests.post('http://<REPLACE WITH IP>/feedback', json=review)
    response.raise_for_status()

if __name__ == '__main__':
    files_dir = 'data/feedback'
    for file in os.listdir(files_dir):
        review = process_file(files_dir + '/' + file)
        upload_file(review)
