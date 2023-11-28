# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:54:39 2022

@author: yjeon
"""

list0 = [10, 20, 30, 40, 50]

list = [sum(list0[:x+1]) for x in range(5)]

print(list)