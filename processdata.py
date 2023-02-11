from PIL import Image
import numpy
import glob
import re
from natsort import natsorted
list_of_files = glob.glob('E:/GeneralDev/chronicon-ai/data/*jpg')
list_of_files = natsorted(list_of_files)
data = []
actions = []
if(len(list_of_files) != 0):
	for file in list_of_files:
		with Image.open(file) as image:
			#image = image.resize((128,128))
			#image.save('E:/GeneralDev/chronicon-ai/data/'+re.findall(r'(?<=\\)\w.+',file)[0])
			image = numpy.asarray(image.getdata(), dtype=int)
			action = re.findall(r'(?<=\')\w+(?=\')', file)
			if(action[0].isdigit()):
				actions = numpy.append(actions, action[0])
			else:
				actions = numpy.append(actions, (ord(action[0])))
			data.append(image)
data = numpy.array(data)
actions = numpy.array(actions)
numpy.save("frames", data)
numpy.save("actions", actions)