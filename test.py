import numpy
from PIL import Image
from pynput.mouse import Button

with Image.open("file.jpg") as im:
	im = im.convert("L")
	with open("data.txt", "w") as data:
		data.write(str(list(im.getdata())))
		array=numpy.asarray(im.getdata())
