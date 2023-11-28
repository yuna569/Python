# -*- coding: utf-8 -*-
"""
Created on Thu May 12 19:49:38 2022

@author: yjeon
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

tran = []

for i in range(len(matrix[0])):
    tran_row = []
    for row in matrix:
        tran_row.append(row[i])
    tran.append(tran_row)
            
print(tran)