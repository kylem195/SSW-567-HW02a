# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Tests a variety of Right traingle scenarios
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
            
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(3,5,4),'Right','3,5,4 is a Right triangle')
        
    def testRightTriangleD(self):
        self.assertEqual(classifyTriangle(5,4,3),'Right','5,4,3 is a Right triangle')
        
    def testRightTriangleE(self):
        self.assertEqual(classifyTriangle(3/3,5/3,4/3),'Right','3/3,5/3,4/3 is a Right triangle')
        
    # Tests a variety of Equilateral triangle scenarios
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        
    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(7,7,7),'Equilateral','7,7,7 should be equilateral')
        
    def testEquilateralTriangleC(self):
        self.assertEqual(classifyTriangle(4.97,4.97,4.97),'Equilateral','4.97,4.97,4.97 should be equilateral')
        
    def testEquilateralTriangleD(self):
        self.assertEqual(classifyTriangle(1/3,1/3,1/3),'Equilateral','1/3,1/3,1/3 should be equilateral')
        
    # Tests a variety of Isosceles triangle scenarios
    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(1,2,2),'Isoceles','1,2,2 should be Isoceles')
        
    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(1.5,1,1.5),'Isosceles','1.5,1,1.5 should be Isosceles')
        
    def testIsocelesTriangleC(self):
        self.assertEqual(classifyTriangle(1.5,1.5,.5),'Isosceles','1.5,1.5,.5 should be Isosceles')
        
    def testIsocelesTriangleD(self):
        self.assertEqual(classifyTriangle(1,2/3,2/3),'Isosceles','1,2/3,2/3 should be Isosceles')
        
    # Tests a variety of Scalene triangle scenarios
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(1,2,3),'Scalene','1,2,3 should be Scalene')
        
    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(2,3,1),'Scalene','2,3,1 should be Scalene')
        
    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(3,2,1),'Scalene','3,2,1 should be Scalene')
        
    def testScaleneTriangleD(self):
        self.assertEqual(classifyTriangle(1.7,2/3,1.34),'Scalene','1.7, 2/3, 1.34 should be Scalene')
        
    def testScaleneTriangleE(self):
        self.assertEqual(classifyTriangle(10,2.6,8.7),'Scalene','10, 2.6, 8.7 should be Scalene')
        
    # Tests a variety of Not a traingle (and invalid entry) scenarios
    def testInvalidTriangleA(self):
        self.assertNotEqual(classifyTriangle('1',2,4), 'Invalid Entry', 'Strings are valid entries if convertible to float')
        
    def testInvalidTriangleB(self):
        self.assertEqual(classifyTriangle('1',2,4), 'Not A Triangle','1,2,4 cannot form a triangle')
        
    def testInvalidTriangleC(self):
        self.assertEqual(classifyTriangle('X',2,4), 'Invalid Entry','Strings not convertible to float are not valid')
        
    def testInvalidTriangleD(self):
        self.assertEqual(classifyTriangle(-1,2,4), 'Invalid Entry','Negative numbers are not valid entries')
        
    def testInvalidTriangleE(self):
        self.assertEqual(classifyTriangle(1,2,10), 'Not A Triangle','1,2,10 cannot form a triangle')
        
    def testInvalidTriangleF(self):
        self.assertEqual(classifyTriangle(11.45,2/3,5.6), 'Not A Triangle','11.45,2/3,5.6 cannot form a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

