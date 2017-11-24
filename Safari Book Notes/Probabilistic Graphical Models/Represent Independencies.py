# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:05:33 2017

@author: cdonovan
"""

import pgmpy

help(pgmpy)

# Represent Independencies
from pgmpy.independencies import IndependenceAssertion

# Each assertion is in the form of [X, Y, Z] meaning X is independent of Y given Z.
assertion1 = IndependenceAssertion('X','Y') # X is independent of Y
assertion1

# Conditional Assertion
assertion2 = IndependenceAssertion('X','Y','Z') # X independent of Y given Z
assertion2

assertion3 = IndependenceAssertion('X',['Y','Z'],['A','B'])
assertion3

# Independencies class used to represent set of assertions
from pgmpy.independencies import Independencies

# Can either: 1. Initialize empty object & add assertions or 2. Initialize with some assertions
# Method 1
independencies = Independencies()
independencies.get_assertions()
independencies.add_assertions(assertion1, assertion2)
independencies.get_assertions()

# Method 2
independencies = Independencies(assertion1, assertion2)
independencies.get_assertions()
independencies = Independencies(['X', 'Y'],['A', 'B', 'C'])
independencies.get_assertions()