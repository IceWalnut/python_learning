import numpy as np
import matplotlib.pyplot as plt

x = np.array([[0., 1.],[1., 1.], [2., 1.], [3., 1.]])
y = np.array([-1, 0.2, 0.9, 2.1])
m, c = np.linalg.lstsq(x, y)[0]

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.legend()
plt.show()
