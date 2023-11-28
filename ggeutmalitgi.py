# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:27:03 2022

@author: yjeon
"""

game = []

connect = True
s = input("끝말잇기 시작: ")
game.append(s)

while connect == True:
    l = int(len(s)) - 1
    n = input(f"{game}, ")
    if len(n) == 1:
        connect = False
    elif n[0] == s[l]:
        game.append(n)
        s = n
    else:
        connect = False
        
print(game)