from PIL import Image

img = Image.open('/media/amey/New Volume/Programs_Python/img_name.jpeg')


# RESIZE *************************

square_img = img.resize((600, 600))
#square_img.show()


# FLIP IMAGE *********************

flip_img = img.transpose(Image.FLIP_TOP_BOTTOM)		# FLIP_LEFT_RIGHT also possible
#flip_img.show()


# ROTATE IMAGE *******************

rotate_img = img.transpose(Image.ROTATE_90)		# ROTATE_180 and ROTATE_270 also possible
rotate_img.show()