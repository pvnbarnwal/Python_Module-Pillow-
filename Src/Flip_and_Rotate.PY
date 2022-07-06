"""Image.FLIP_LEFT_RIGHT – For flipping the image horizontally
Image.FLIP_TOP_BOTTOM – For flipping the image vertically
Image.ROTATE_90 – For rotating the image by specifying degree"""


# Horizontally flipped Image
# import required image module
from PIL import Image
# Open an already existing image
imageObject = Image.open("Image/Boy.jpg")
# Do a flip of left and right
hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
# Show the original image
# imageObject.show()
# Show the horizontal flipped image
# hori_flippedImage.show()


# Vertically Flipped Image
# import required image module
from PIL import Image
# Open an already existing image
imageObject = Image.open("Image/Boy.jpg")
# Do a flip of left and right
Vert_flippedImage = imageObject.transpose(Image.FLIP_TOP_BOTTOM)
Vert_flippedImage.show()
# Show the original image
# imageObject.show()
