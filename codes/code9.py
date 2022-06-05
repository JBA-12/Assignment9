import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp

n = 64

t = np.linspace(0, 2*np.pi, n+1)


plt.axis("equal")
plt.hlines(1/4, 0, 1, color='black')
plt.hlines(3/4, 1, 2, color='black')
plt.hlines(1, 2, 3.7, color='black')

plt.vlines(1, 1/4, 3/4, color='black')
plt.vlines(2, 3/4, 1, color='black')
plt.xlabel('x')
plt.ylabel('Fx(x)')
plt.legend(loc="upper left")
plt.show()