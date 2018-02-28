import os

from PIL import Image, ImageFont, ImageDraw


size = (160, 160)
size = (88, 65)
im = Image.new("RGB", size)
draw = ImageDraw.Draw(im)

fonts_dir = os.path.expanduser('~/.fonts/Fonts/Microsoft')

# font_telugu = ImageFont.truetype(os.path.join(fonts_dir, "Pothana2001.ttf"), 50)
font_telugu = ImageFont.truetype(os.path.join(fonts_dir, "Vani.ttf"), 50)
text_telugu = "నిత్య"
w, h = draw.textsize(text_telugu, font=font_telugu)
draw.text((w, h), text_telugu, font=font_telugu)
draw.text((0, 0), text_telugu, font=font_telugu)


print(w, h)
im.show()
