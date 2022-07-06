from PIL import ImageColor
# # using getrgb
# img = ImageColor.getrgb("blue")
# print(img)



# #Import required image modules
# from PIL import Image,ImageColor
# # Create new image & get color RGB tuple.
# img = Image.new("RGB", (256, 256), ImageColor.getrgb("#add8e6"))
# #Show image
# img.show()


from PIL import Image,ImageColor
# using getrgb
img = ImageColor.getrgb("skyblue")
print(img)
img1 = ImageColor.getrgb("purple")
print(img1)