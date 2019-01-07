from PIL import Image

img1 = Image.open('/media/amey/New Volume/Programs_Python/img_name.jpeg')
img2 = Image.open('/media/amey/New Volume/Programs_Python/img_test.png')

area = (0, 0, 718, 465)		# Area = area of img2 (img to be combined with), Else error
img1.paste(img2, area)

img1.show()