#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Benjamin Seeley
# Student ID: 2262810
# Email: seele105@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW03
###

"""Contains helper functions that return lists of sequences.
"""

def fibonacci(n):
    """Returns n fibonacci numbers
    Args:
        n: number of fibonacci numbers to return
        
    Returns:
        List that contains n fibonacci numbers
    
    Raises:
        ValueError when n is not a positive integer
    """
    
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    output = []
    f1 = 0
    f2 = 1
    fn = 1
    count = 0
    for i in range(n):
        output.append(fn)
        fn = f1 + f2
        f1 = f2
        f2 = fn
    return output
