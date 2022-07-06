from PIL import Image, ImageDraw
img = Image.open('Image/Boy.jpg')
d1 = ImageDraw.Draw(img)
# 90 96 is position 
d1.text((90, 96), "Hello, Shubham!", fill=(255, 0, 0))
# img.show()



# Selecting the font
from PIL import Image, ImageDraw, ImageFont
# img = Image.open('Image/Boy.jpg')
d1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype('E:/PythonPillow/Fonts/FreeMono.ttf', 40)
d1.text((0, 0), "Sample text", font=myFont, fill =(255, 0, 0))
img.show()
# img.save("images/image_text.jpg")