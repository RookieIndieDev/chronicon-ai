import glob
import numpy
from PIL import Image
from natsort import natsorted

frames = numpy.load("frames.npy")
actions = numpy.load("actions.npy")
files = glob.glob("E:/GeneralDev/chronicon-ai/data/*jpg")
files = natsorted(files)
diff = len(files)-len(frames)

if (diff > 0):
	for file in files[len(frames):len(files)]:
		with Image.open(file) as image:
			image = numpy.asarray(image.getdata(), dtype=int)
			action = re.findall(r'(?<=\')\w+(?=\')', file)
			if(action[0].isdigit()):
				actions = numpy.append(actions, action[0])
			else:
				actions = numpy.append(actions, (ord(action[0])))
			data.append(image)
