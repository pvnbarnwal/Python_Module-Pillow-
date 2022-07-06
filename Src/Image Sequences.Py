from PIL import Image
img = Image.open('Image/Boy.jpg')
#Skip to the second frame
img.seek(1)
try:
    while 1:
        img.seek(img.tell() + 1)
    #do_something to img
except EOFError:
#End of sequence
    pass