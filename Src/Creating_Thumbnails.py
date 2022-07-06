from PIL import Image

try:
    image = Image.open('/home/shubham/Downloads/Workshop/PIL/lyman-hansel-gerona-FV7AEDaW53c-unsplash.jpg')
    image.thumbnail((90,90))
    image.save('thumbnail.jpg')
    image1 = Image.open('thumbnail.jpg')
    image1.show()
except IOError:
    pass

