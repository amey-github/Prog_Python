from PIL import Image

img1 = Image.open('/media/amey/New Volume/Programs_Python/img_name.jpeg')
img2 = Image.open('/media/amey/New Volume/Programs_Python/img_test.png')


print(img1.size, img2.size)
print(img1.mode, img2.mode)

area = (0, 0, 718, 465)
img1_crop = img1.crop(area)			# Else size-mismatch error

#img1_crop.show()

r1, g1, b1 = img1_crop.split()		# MOde is RGB
r2, g2, b2, a2 = img2.split()		# Since its mode is RGBA

new_image = Image.merge('RGB', (r1, b1, b2))
new_image.show()