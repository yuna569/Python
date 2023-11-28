# -*- coding: utf-8 -*-
"""
Created on Thu May 12 18:40:56 2022

@author: yjeon
"""

table = []

def printList(mylist):
    rows = len(mylist)
    cols = len(mylist[0])
    for i in range(rows):
        for j in range(cols):
            print(mylist[i][j], end=" ")
        print()
            
def init(mylist):
    rows = len(mylist)
    cols = len(mylist[0])
    for i in range(rows):
        for j in range(cols):
            if i%2==0:
                if j%2==0:
                    mylist[i][j] = 0
                else: mylist[i][j] = 1
            else:
                if j%2==0:
                    mylist[i][j] = 1
                else: mylist[i][j] = 0
                
for row in range(10):
    table += [[0]*10]
    
init(table)
printList(table)