# -*- coding: utf-8 -*-
"""
Created on Thu May 12 11:52:24 2022

@author: yjeon
"""

from tkinter import *
from tkinter.colorchooser import askcolor

DEFAULT_PEN_SIZE = 1.0
DEFAULT_COLOR = 'black'

mode = "pen"
old_x = None
old_y = None
mycolor = DEFAULT_COLOR
erase_on = False 

def use_pen():
    global mode
    mode = "pen"
    
def use_brush():
    global mode
    mode = "brush"
    
def choose_color():
    global mycolor
    mycolor = askcolor(color=mycolor)
    
def use_pen():
    global mode
    mode = "erase"
    
def paint(event):
    global  var, erase_on, mode, old_x, old_y 
    fill_color = 'white' if mode == "erase" else mycolor
    if old_x and old_y()canvas.create_line(old_x, old_y, )