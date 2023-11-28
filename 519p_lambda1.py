# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:15:26 2022

@author: yjeon
"""

f_temp = [0, 10, 20, 30, 40, 50]
ftoc = lambda c:(5.0/9.0)*(c-32.0)
c_temp = map(ftoc, f_temp)
print(list(c_temp))