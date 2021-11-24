import matplotlib.pyplot as plt
import numpy as np

# 定义三角函数
X=np.linspace(-np.pi,np.pi,360,endpoint=True)
S=np.sin(X)
C=np.cos(X)
T=np.tan(X)
#绘图
plt.plot(X,S)