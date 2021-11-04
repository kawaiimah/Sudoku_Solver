# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:22:08 2020

Solves a Sudoku array specified as df
where 0 is placeholder for unknown digits 

"""

import sys

# Set puzzle
df = []
df.append('123456789')
df.append('000000000')
df.append('000000000')
df.append('000000000')
df.append('000000000')
df.append('000000000')
df.append('000000000')
df.append('000000000')
df.append('000000000')

# Import numbers into integer array
ary = []
for i in range(9):
    temp = []
    for c in df[i]:
        temp.append(int(c))
    ary.append(temp)

# Show user the array and check if ok to proceed
print('\nImported:')
for i in range(9):
    print(ary[i])
if input('\nProceed to solve?').lower() != "y":
    sys.exit()

def possible(y,x,n):

    # This function checks if it is possible for n to be at position y,x
    
    global ary
   
    # Check if n already exists in the same column or row
    for i in range(9):
        if ary[y][i]==n or ary[i][x]==n:
            return False

    # Check if n already exists in the 3x3 block
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if ary[y0+j][x0+i]==n:
                return False

    return True


def solve():

    # Main recursive function that steps thru the array looking for 0,
    # tries n from 1 to 9 in that position, then calls itself again
    # for the rest of the array
    
    global ary

    for y in range(9):
        for x in range(9):
            if ary[y][x]==0:
                for n in range(1,10):
                    if possible(y,x,n):
                        ary[y][x] = n
                        solve()
                        ary[y][x] = 0
                return

    # Prints solution once no more 0's are found
    for i in range(9):
        print(ary[i])

    if input('Try to see if another solution exists?').lower() != "y":
        sys.exit()

# Take a deep breath, start the ball rolling!
solve()