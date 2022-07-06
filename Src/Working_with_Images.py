from PIL import Image


# Reading an Image

x=Image.open('field-gfa91f85d4_1920.jpg', mode='r')
print(x)
# fp: A filename (string), pathlib.Path object or a file object. The file object must implement read(), seek() and tell() methods and be opened in binary mode.
# mode: It’s an optional argument, if given, must be ‘r’.
# Return value: An Image object.
# Error: If the file cannot be found, or the image cannot be opened and identified

image = Image.open('field-gfa91f85d4_1920.jpg')
image.show()
image.save('field-gfa91f85d4_1920.jpg.bmp')
image1 = Image.open('field-gfa91f85d4_1920.jpg.bmp')
image1.show()





