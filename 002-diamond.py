#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 20:39:40 2020

@author: kant
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
