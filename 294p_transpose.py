# -*- coding: utf-8 -*-
"""
Created on Thu May 12 19:15:52 2022

@author: yjeon
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

tran = []

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if row == col:
            tran.append(matrix[row][col])
        else:
            tran.append(matrix[col][row])
            
print(tran)