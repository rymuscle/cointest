#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 下午7:19
# @Author  : RenYimin
# @Site    : 
# @File    : Demo.py
# @Software: PyCharm

from decimal import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

# x
x = 18900   #todo 价格不定

q1 = []
for num in range(3, 20):
    q1.append(num*0.1)
for num in range(3, 10):
    q1.append(num)
q1 = np.array(q1)
print(q1)

# z 一小时
z1 = 6.5 * 90 # todo 每小时价格不定

# y
# y*(q-0.2)*0.01 - z > 0
y1 = z1 / ((q1-0.2)*0.01)

plt.plot(q1, y1, color="blue", linewidth=1.0, linestyle="-")

x_major_locator=MultipleLocator(0.5)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
# plt.xlabel('Numbers',fontsize=9)

# 设置横轴的上下限
plt.xlim(0.3, 10)
plt.ylim(0, 1000000)

# 幅度
q = []
for num in range(5, 20):
    q.append(num*0.1)
for num in range(5, 10):
    q.append(num)
q = np.array(q)
print(q)

# z 一小时
z = 6.5 * 90 # todo 每小时价格不定

# down, if want to get 。。。
# (x*q*0.01*6.5 - z) - y*(q+0.2)*0.01 > 0
y = (x*q*0.01* 6.5 - z) / ((0.2 + q)*0.01)

plt.plot(q, y, color="green", linewidth=2.0, linestyle="--")

x_major_locator=MultipleLocator(0.5)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.show()
