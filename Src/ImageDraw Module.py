"""The ‘ImageDraw’ module provides simple 2D graphics support for Image Object.
Generally, we use this module to create new images, annotate or retouch existing images
and to generate graphics on the fly for web use."""

#Import required libraries
# import sys
from PIL import Image, ImageDraw
#Create Image object
base = Image.open("Image/1.png")
#Draw line
# draw = ImageDraw.Draw(im)
# draw.line((0, 0) + im.size, fill=128)
# draw.line((0, im.size[1], im.size[0], 0), fill=3000)
#Show image
# im.show()





#Import required modules from Pillow package
from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('Image/Boy.jpg').convert('RGBA')
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))
# get a font
fnt = ImageFont.truetype('E:/PythonPillow/Fonts/Pacifico.ttf', 40)
# get a drawing context
d = ImageDraw.Draw(txt)
# draw text, half opacity
d.text((14,14), "Tutorials", font=fnt, fill=(255,255,255,128))
# draw text, full opacity
d.text((14,60), "Point", font=fnt, fill=(255,255,255,255))
out = Image.alpha_composite(base, txt)
#Show image
out.show()