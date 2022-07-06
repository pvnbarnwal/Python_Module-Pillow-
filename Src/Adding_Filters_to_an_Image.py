from PIL import Image, ImageFilter
im = Image.open('Image/1.png')
im1 = im.filter(ImageFilter.BLUR)
# im1.show()
im2 = im.filter(ImageFilter.MinFilter(3))
# im2.show()
im3 = im.filter(ImageFilter.MinFilter)
# same as MinFilter(3)
# im3.show()









"""Filters
The current version of pillow library provides below mentioned set of predefined image
enhancement filters.
 BLUR
 CONTOUR
 DETAIL
 EDGE_ENHANCE
 EDGE_ENHANCE_MORE
 EMBOSS
 FIND_EDGES
 SHARPEN
 SMOOTH
 SMOOTH_MORE"""




#Import required image modules
from PIL import Image, ImageFilter
#Import all the enhancement filter from pillow
from PIL.ImageFilter import (
BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)
#Create image object
img = Image.open('Image/1.png')
#Applying the blur filter
img1 = img.filter(CONTOUR)
# img1.save('images/ImageFilter_blur.jpg')
img1.show()