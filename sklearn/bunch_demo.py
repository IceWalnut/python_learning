# https://blog.csdn.net/kancy110/article/details/73715739

from sklearn.datasets import _base

buch = _base.Bunch(A=1,B=2,C=3)

type(buch)

buch

buch['A']

dt = {'A':1, 'B':2, 'C':3}

type(dt)

dt['A']

buch.A
dt.A