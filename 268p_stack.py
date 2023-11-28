# -*- coding: utf-8 -*-
"""
Created on Thu May 12 15:33:19 2022

@author: yjeon
"""

stack = []

for i in range(3):
    f = input("과일을 입력하시오: ")
    stack.append(f)
    
#for i in range(3):
 #   print(stack.pop())
 
a = stack.pop()
print(a)