import matplotlib.pyplot as plt
from sklearn import datasets

# 载入数据集
X_train, y_train = datasets.load_breast_cancer(return_X_y=True)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, marker='o', s=40)
