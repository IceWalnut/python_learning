import numpy as np

np.linspace(2.0, 3.0, num=5)

data2 = np.linspace(2.0, 3.0, num=5, endpoint=False)
print(data2)
data3 = np.linspace(2.0, 3.0, num=5, retstep=True)
print(data3)