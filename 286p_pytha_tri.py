# -*- coding: utf-8 -*-
"""
Created on Thu May 12 18:09:29 2022

@author: yjeon
"""

list = [(x, y, z) for x in range(1, 31) for y in range(1, 31) for z in range(1, 31) if x**2+y**2==z**2 and x+y>z and x<=y] 

print(list)