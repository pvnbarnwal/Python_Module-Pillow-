


from PIL import Image, ImageFilter

# Simple blur
# syntax filter(ImageFilter.BLUR)
#Open existing image
OriImage = Image.open('Image/Boy.jpg')
# OriImage.show()
blurImage = OriImage.filter(ImageFilter.BLUR)
# blurImage.show()
#Save blurImage
# blurImage.save('images/simBlurImage.jpg')


#Box Blur
#In this filter, we use ‘radius’ as parameter. Radius is directly proportional to the blur value.
#syntax ImageFilter.BoxBlur(radius)
#Open existing image
OriImage = Image.open('Image/Boy.jpg')
# OriImage.show()
#Applying BoxBlur filter
boxImage = OriImage.filter(ImageFilter.BoxBlur(5))
# boxImage.show()
#Save Boxblur image
# boxImage.save('images/boxblur.jpg')




# Gaussian Blur
#syntax ImageFilter.GaussianBlur(radius=2)
'''This filter also uses parameter radius and does the same work as box blur with some
algorithmic changes. In short, changing the radius value, will generate different intensity
 of ‘Gaussianblur’ images'''
OriImage = Image.open('Image/Boy.jpg')
# OriImage.show()
#Applying GaussianBlur filter
gaussImage = OriImage.filter(ImageFilter.GaussianBlur(5))
gaussImage.show()
#Save Gaussian Blur Image
# gaussImage.save('images/gaussian_blur.jpg')

