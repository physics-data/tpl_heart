import numpy as np
import matplotlib.pyplot as plt

xvals = np.arange(-1, 1, 0.001)

def f(x):
    x = np.abs(x)
    if x > 1e-4 and (x ** x) ** 2 < 1:
        return (1 - (x ** x) ** 2) ** 0.5 + 2
    else:
        return 2

def g(x):
    if np.abs(x) > 1e-4:
        return 2 - (1 - 1.61 * np.arctan(x) ** 2) ** 0.5
    else:
        return 1

plt.plot(xvals, list(map(f, xvals)))
plt.plot(xvals, list(map(g, xvals)))
plt.savefig('heart.png')