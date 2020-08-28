#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 20:39:40 2020

@author: kant

# Daily Challenge #2 - String Diamond

Your task is to return a string that displays a diamond shape on the screen 
using asterisk (“*”) characters.


The shape that the print method will return should resemble a diamond. A number 
provided as input will represent the number of asterisks printed on the middle 
line. The line above and below will be centered and will have two less 
asterisks than the middle line. This reduction will continue for each line 
until a line with a single asterisk is printed at the top and bottom of the 
figure.

Return null if input is an even number or a negative number.

Note: JS and Python students must implement diamond() method and return 
None (Py) or null(JS) for invalid input.
"""

def diamond(n:int):
    if n%2 == 0:
        return None
    
    spaces = range(int((n-1)/2),-1,-1)
    asterisks = range(1,n+1,2)
    
    result = ''
    for i,j in zip(spaces,asterisks):
        result = result + ' '*i + '*'*j + '\n'
    
    spaces  = range(1,int((n-1)/2)+1)
    asterisks = range(n-2,0,-2)
    for i,j in zip(spaces,asterisks):
        result = result + ' '*i + '*'*j + '\n'
    result = result[:-1]
    return result
