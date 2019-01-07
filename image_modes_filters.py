from PIL import Image
from PIL import ImageFilter


img = Image.open('/media/amey/New Volume/Programs_Python/img_test.png')
print(img.mode)

# CHANGE IMAGE MODE ***************

img_rgb = img.convert('RGB')
img_rgb.show()
print(img_rgb.mode)


# CHANGE IMAGE TO BLACH & WHITE ***

img_bw = img.convert('L')
img_bw.show()
print(img_bw.mode)


# IMAGE EFFECTS********************

img_blur = img.filter(ImageFilter.BLUR)
img_blur.show()

img_detail = img.filter(ImageFilter.DETAIL)
img_detail.show()

img_edges = img.filter(ImageFilter.FIND_EDGES)
img_edges.show()