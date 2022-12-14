from matplotlib import pyplot as plt
import numpy as np

t = np.linspace(0, np.pi*50, 10000)

x = np.sin(t/9)**3
y = np.cos(t)**2-np.sin(t*50)*np.cos(t*2)**2


plt.figure(figsize=(20, 20))
plt.plot(x, y)
plt.savefig('out/test.png')