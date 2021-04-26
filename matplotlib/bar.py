import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as ps

x = np.linspace(0, 2, 100)

mytuple = plt.subplots()
ax = mytuple[1]
ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratic')
ax.plot(x, x**3, label='cubic')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple Plot")
ax.imshow()
