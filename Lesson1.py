#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 00:20:16 2017

@author: vinaya
"""
import numpy as np

a = np.array([1,2,3,4,5])

b = np.arange(1,9,2)

#points between 2 numbers
c = np.linspace(0,1,6)

d = np.ones((3,3))

e = np.eye(3,2)

f = np.diag([1,2,3,4])

g = np.array([1+2j, 3+4j, 5+6*1j])

#arange
a  = np.arange(10)

#reverse
b = a[::-1]

#slice array
c = a[:5]

#start slicing at other index
d = a[2:4]

#start at index end at last index
e = a[3:]

a[5:]= c[::-1]