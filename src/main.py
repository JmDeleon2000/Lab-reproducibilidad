from matplotlib import pyplot as plt
import numpy as np

t = np.linspace(0, np.pi*50, 10000)

sqrt6 = np.sqrt(6)
sqrt3 = np.sqrt(3)
x = (np.cos(sqrt6*t)-np.cos(sqrt3*t)+5*np.sin(sqrt3*t)/sqrt3-34*np.sin(sqrt6*t)/sqrt6)/4
y = -3*np.sin(sqrt3*t)/sqrt3


plt.figure(figsize=(20, 20))
plt.plot(x, y)
plt.savefig('out/test.png')