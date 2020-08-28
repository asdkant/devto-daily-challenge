#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 21:14:10 2020

@author: kant

# Challenge

Write a function that returns the number (count) of vowels in a given string. 
Letters considered as vowels are: a, i, e, o, and u. The function should be 
able to take all types of characters as input, including lower case letters, 
upper case letters, symbols, and numbers.

"""

def vowcount(s:str, vowels='aeiou'):
    result = 0
    for l in s:
        if l in vowels: result+=1
    return result