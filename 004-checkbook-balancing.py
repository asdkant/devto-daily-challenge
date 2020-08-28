#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 21:29:51 2020

@author: kant

https://dev.to/thepracticaldev/daily-challenge-4-checkbook-balancing-hei

# Daily Challenge #4 - Checkbook Balancing

You are given a small checkbook to balance that is given to you as a string. 
Sometimes, this checkbook will be cluttered by non-alphanumeric characters.

The first line shows the original balance. Each other (not blank) line gives 
information: check number, category, and check amount.

You need to clean the lines first, keeping only letters, digits, dots, and 
spaces. Next, return the report as a string. On each line of the report, you 
have to add the new balance. In the last two lines, return the total expenses 
and average expense. Round your results to two decimal places.

Example Checkbook
    1000.00
    125 Market 125.45
    126 Hardware 34.95
    127 Video 7.45
    128 Book 14.32
    129 Gasoline 16.10

Example Solution
    Original_Balance: 1000.00
    125 Market 125.45 Balance 874.55
    126 Hardware 34.95 Balance 839.60
    127 Video 7.45 Balance 832.15
    128 Book 14.32 Balance 817.83
    129 Gasoline 16.10 Balance 801.73
    Total expense 198.27
    Average expense 39.65

Challenge Checkbook
    1233.00
    125 Hardware;! 24.8?;
    123 Flowers 93.5
    127 Meat 120.90
    120 Picture 34.00
    124 Gasoline 11.00
    123 Photos;! 71.4?;
    122 Picture 93.5
    132 Tires;! 19.00,?;
    129 Stamps 13.6
    129 Fruits{} 17.6
    129 Market;! 128.00?;
    121 Gasoline;! 13.6?;
"""

import string

def balance(checkbook:str) -> str:
    cleanchars = string.ascii_letters+string.digits+' .\n'
    clean_checkbook = ''.join(
        [i for i in checkbook if i in cleanchars]).strip('\n')
    original_balance = float(clean_checkbook.split('\n')[0])
    balance = original_balance
    entries = clean_checkbook.split('\n')[1:]
    result = f'Original_Balance: {original_balance:.2f}'
    for e in entries:
        entry_spend = float(e.split(' ')[-1])
        balance -= entry_spend
        result += f'\n{e} Balance {balance:.2f}'
    
    total_expense = original_balance - balance
    result += f'\nTotal expense {total_expense:.2f}'
    average_expense = total_expense / len(entries)
    result += f'\nAverage expense {average_expense:.2f}'
    return result

    












