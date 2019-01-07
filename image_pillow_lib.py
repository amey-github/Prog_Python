from PIL import Image		# PIL (Pillow): library that help us work with images

img = Image.open('/media/amey/New Volume/Programs_Python/img_name.jpeg')	# img object needed to work with images, similar to text file

print(img.size)
print(img.format)

img.show()	# Images can't be opened in terminal, NOTICE: name of img file opened is diff from img_name
			# show() creates a temporary copy of the img_name, saves it and displays it using the default application