import numpy as np
import scipy as sp
from scipy.optimize import leastsq

# 目标函数
def func(x):
    return 2 * np.sin(2*np.pi*x)

# 残差函数
def residuals(p, x, y):
    # poly1d 按照输入的列表 p 生成一个多项式函数
    fun = np.poly1d(p)
    return y - fun(x)

# 拟合函数
def fitting(p):
    # 生成 p + 1 个随机数的列表，这样 poly1d 函数返回的多项式次数就是 p
    pars = np.random.rand(p + 1)
    # 三个参数： 误差函数、函数参数列表、数据点
    r = leastsq(residuals, pars, args=(X, Y))
    return r
