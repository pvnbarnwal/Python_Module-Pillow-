# python -m pip install pillow

from PIL import Image

# 3.Python Pillow — Using Image Module    
# Opening, rotating and displaying an image       
# Attributes of Image Module      

image=Image.open('/home/shubham/Downloads/Workshop/PIL/field-gfa91f85d4_1920.jpg')

# im.show()

image.rotate(45).show()

#  It returns a dictionary holding data associated with the image.
image.info
image.filename
image.format

'''A color palette, in the digital world, refers to the full range of colors that can be displayed on a device screen or other interface, or in some cases, a collection of colors and tools for use in paint and illustration programs.'''
print(image.filename,image.palette)

image.mode  #It is used to get the pixel format used by the image. Typical values are “1”, “L”, “RGB” or “CMYK”
image.size
image.width
image.height
image.palette      # It returns the colour palette table, if any.