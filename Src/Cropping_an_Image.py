from PIL import Image
#Create an Image Object from an Image
im = Image.open('Image/Boy.jpg')
#Display actual image
# im.show()
#left, upper, right, lower
#Crop
cropped = im.crop((1,2,300,300))
#Display the cropped portion
cropped.show()
#Save the cropped image
# cropped.save('images/croppedBeach1.jpg')