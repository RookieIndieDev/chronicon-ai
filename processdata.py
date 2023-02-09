from PIL import Image
import numpy
import glob
import re
list_of_files = glob.glob('E:/GeneralDev/Chronicon AI/data/*')
data = []

if(len(list_of_files) != 0):
	for file in list_of_files:
		with Image.open(file) as img:
			image = numpy.asarray(img.getdata(), dtype=int)
			action = re.findall(r'(?<=\')\w+(?=\')', file)
			if(action[0].isdigit()):
				image = numpy.append(image, action[0])
			else:
				image = numpy.append(image, (ord(action[0])))
			data.append(image)
data = numpy.array(data)
print(data[0])
numpy.save("data", data)