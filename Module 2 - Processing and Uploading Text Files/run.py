#! /usr/bin/env python3

import os
import requests

if __name__ == '__main__':
    for files in os.listdir('data/feedback'):
        review = processFile(file)
        uploadFile(review)
