import numpy as np
# data = np.array([[1,2,1],[0,3,1],[2,1,4],[1,4,1]])
# np.sum(data, axis=1)

# np.min(data, axis=0)

# np.average(data)

# 四维数组
data = np.random.randint(0, 5, [4,3,2,3])
# data = np.random.randint(0, 5, [3, 2])
print(data)

print("axis=0")
print(data.sum(axis = 0))
print("axis=1")
print(data.sum(axis = 1))
print("axis=2")
print(data.sum(axis = 2))
print("axis=3")
print(data.sum(axis = 3))
