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

q = []
for num in range(3, 20):
    q.append(num*0.1)
for num in range(3, 10):
    q.append(num)
q = np.array(q)
print(q)

# z 一小时
z = 6.5 * 90 # todo 每小时价格不定

# y
# y*(q-0.2)*0.01 - z > 0
y = z / ((q-0.2)*0.01)

plt.plot(q, y, color="blue", linewidth=1.0, linestyle="-")

x_major_locator=MultipleLocator(0.5)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
# plt.xlabel('Numbers',fontsize=9)

# 设置横轴的上下限
plt.xlim(0.3, 10)
plt.ylim(0, 1000000)
plt.title("up")
plt.show()
