# -*- coding: utf-8 -*-
"""
Created on Thu May 12 20:02:16 2022

@author: yjeon
"""

board = [[" " for i in range(3)] for j in range(3)]

while True:
    for r in range(3):
        print(" " + board[r][0] + "/ " + board[r][1] + "/ " + board[r][2])
        if r != 2:
            print("--/--/--")
    
    x = int(input("x: "))
    y = int(input("y: "))

    if board[x][y] != " ":
        print("이미 선택된 칸")
        continue
    else:
        board[x][y] = "X"
    
    done = False

    for i in range(3):
        for j in range(3):
            if board[i][j] == " " and not done:
                board[i][j] = "O"
                done = True
                break
    
