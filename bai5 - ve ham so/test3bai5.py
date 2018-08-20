import numpy as np
from numpy import *
import math
import matplotlib.pyplot as plt

# f(x) = (e^(−x/10))*sin(πx)
x1 = np.arange(0, 10, 0.01)
y1 = np.power(np.e, (-x1/10)) * np.sin(np.pi * x1) 
# x*e^(−x/3)
y2 = np.power(x1*np.e , (-x1/3))

plt.plot(x1, y1, 'r',label = 'f(x)')
plt.plot(x1, y2 , 'b', label ='g(x)')
plt.legend()

plt.plot()

plt.ylabel("long")
plt.xlabel("latt")


plt.savefig("plot.png")
