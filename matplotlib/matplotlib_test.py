import numpy as np
from matplotlib import pyplot as plt
import matplotlib

x = np.arange(1, 11)
y = 2 * x + 5

plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
# o 是圆标记 b 是蓝色
plt.plot(x, y, "ob")
plt.show()