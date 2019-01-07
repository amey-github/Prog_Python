from PIL import Image

img = Image.open('/media/amey/New Volume/Programs_Python/img_name.jpeg')

area = (200, 200, 300, 375)			# (x1, y1, x2, y2) : (top_left_coord, bottom_right_coord)
cropped_img = img.crop(area)

img.show()
cropped_img.show()