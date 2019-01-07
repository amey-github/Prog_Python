from PIL import Image

img = Image.open('/media/amey/New Volume/Programs_Python/img_name.jpeg')

print(img.mode)			# Images are made up of diff layers of colours (channels) R, G, B
r, g, b = img.split()	# Splits an image into individual channels

'''
r.show()
g.show()
b.show()
'''

#new_img = Image.merge('RGB', (r, g, b))
new_img = Image.merge('RGB', (b, g, r))		# GOOD SHIT
new_img.show()