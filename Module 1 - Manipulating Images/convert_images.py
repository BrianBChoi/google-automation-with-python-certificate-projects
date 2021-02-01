#!/usr/bin/env python3

from PIL import Image
import os

for file in os.listdir('images'):
    # This file is not an image
    if file == '.DS_Store':
       continue
    
    image = 'images/' + file
    im = Image.open(image)
    new_im = im.rotate(270).resize((128,128)).convert('RGB')
    new_im.save('opt/icons/' + file, 'JPEG')
