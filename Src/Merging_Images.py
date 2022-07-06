# Syntext   Image.merge(mode, bands)

# Using the merge() function, you can merge the RGB bands of an image as

from PIL import Image
# image = Image.open("1.png")
# r, g, b,x =(image.split())
# image.show()
# image = Image.merge("RGB", (x,b, g, r))
# image.show()



image1 = Image.open('Image/1.png')
# image1.show()
image2 = Image.open('Image/2.png')
# image2.show()

#resize, first image
image1 = image1.resize((426, 240))
# print(image1.size)
# image1.show()

new_image = Image.new('RGB',(2*image1.size[0], image1.size[1]), (250,250,250)) #Background of light color Layer 1

new_image.paste(image1,(0,0))
new_image.paste(image2,(image1.size[0],0))
new_image.save("merged_image.jpg","JPEG")
# new_image.show()