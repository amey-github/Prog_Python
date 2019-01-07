from PIL import Image

img = Image.open('/media/amey/New Volume/Programs_Python/img_name.jpeg')
wrinkle = Image.open('/media/amey/New Volume/Programs_Python/img_wrinkle.jpg')


print(img.size, wrinkle.size)
print(img.mode, wrinkle.mode)

area = (0, 0, 1023, 683)
img_crop = img.crop(area)

#img_crop.show()

r1, g1, b1 = img_crop.split()
r2, g2, b2 = wrinkle.split()

new_image = Image.merge('RGB', (r1, g2, b2))
new_image.show()