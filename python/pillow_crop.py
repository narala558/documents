import os
import sys

from PIL import Image


x = (275, 55)
y = (1095, 715)
box = (*x, *y)

for fname in os.listdir('.'):
    img = Image.open(fname)
    img = img.crop(box)
    fname = fname.zfill(2)
    img.save(fname)
