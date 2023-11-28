# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:36:08 2022

@author: yjeon
"""

import time
SIZE = 50000

start_time = time.time()
mylist = []
for i in range(SIZE):
    mylist = mylist + [i**2]
print("수행 시간: ", time.time() - start_time)

start_time = time.time()
mylist = []
for i in range(SIZE):
    mylist.append(i**2)
print("수행 시간: ", time.time() - start_time)