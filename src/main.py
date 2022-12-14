from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

t = np.linspace(0, np.pi*50, 10000)

sqrt6 = np.sqrt(6)
sqrt3 = np.sqrt(3)
x = (np.cos(sqrt6*t)-np.cos(sqrt3*t)+5*np.sin(sqrt3*t)/sqrt3-34*np.sin(sqrt6*t)/sqrt6)/4
y = -3*np.sin(sqrt3*t)/sqrt3


plt.figure(figsize=(20, 20))
plt.plot(x, y)

outPath = 'out/test.png'
plt.savefig(outPath)

img = Image.open(outPath)

newData = []
for item in img.getdata:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 0, 0, 255))
    else:
        newData.append(item)

img.putdata(newData)
img.save(outPath, "PNG")