import os

from PIL import Image, ImageFont, ImageDraw, ImageChops
import numpy as np
from pylab import *


filename = 'f.png'


Image.fromarray(np.empty((0, 0), dtype=np.uint8))

# img = Image.open('foo.jpg')
# new_width, new_height = 0, 0
# img = img.resize((1, 1), Image.ANTIALIAS)
# img.save('bar.jpg')


# convert image to np array
in_data = np.asarray(im, dtype=np.uint8)
img = Image.open('f.png')
print(img.size)
#img.show()
wd, ht = img.size
pix = np.array(img.convert('1').getdata(), np.uint8)
bimg = 1 - (pix.reshape((ht, wd)) / 255.)

plt.imshow(bimg)
plt.show()


#image.show()
#image = np.asarray(image, dtype=np.uint8)

print(bimg.shape)
dimg = rdistort(bimg, cval=100)


plt.imshow(bimg)
plt.show()


# crop image
left = 20
upper = 30
right = 10
lower = 15
box = (left, upper, right, lower)

img = Image.open(filename)
img = img.crop(box)
img.save(filename)


# trim whitespace
def trim(img):
    bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    if bbox:
        trimmed_img = img.crop(bbox)
    else:
        trimmed_img = img

    return trimmed_img


img = trim(img)
img.show()


# render text on image
size = (88, 65)
img = Image.new("RGB", size)
draw = ImageDraw.Draw(img)

fonts_dir = os.path.expanduser('~/.fonts/Fonts/Microsoft')
font_telugu = ImageFont.truetype(os.path.join(fonts_dir, "Vani.ttf"), 50)
text_telugu = "నిత్య"
w, h = draw.textsize(text_telugu, font=font_telugu)
draw.text((w, h), text_telugu, font=font_telugu)
draw.text((0, 0), text_telugu, font=font_telugu)

print(w, h)
img.show()
