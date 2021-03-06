# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # All entries must be convertible to floats, othwerwise they are invalid
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except:
        return 'Invalid Entry'

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'Invalid Entry'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'Invalid Entry'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # or the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'Not A Triangle'
        
    # now we know that we have a valid triangle 
    epsilon = .0000001
    if a == b and b == c and c == a:
        return 'Equilateral'
    elif (abs(a**2 + b**2 - c**2) < epsilon or
          abs(b**2 + c**2 - a**2) < epsilon or
          abs(c**2 + a**2 - b**2) < epsilon):
        return 'Right'
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isosceles'
