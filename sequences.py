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

This docstring should contain an overview and purpose of the code being
written below, as well as example uses (if appropriate).
"""

def fibonacci(n):
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
    """Function docstring
    
    All functions should have their own documentation via docstrings.
    Function arguments are positional, unless they are provided a default 
    value to become a "keyword argument".
    Here args is a list of all positional arguments beyond those listed.
    Here kwargs is a list of all keyword arguments beyond those listed.
    
    The function doc string should describe the name of the function, 
    its return value and type (if any), and its list of arguments and
    their expected types (if any). Both positional and keyword arguments
    should be listed separately.
    
    For more detailed examples from Google about how to use docstrings see,
    http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    
    All indentation should be 4 spaces.  NO TABS IN PYTHON CODE.
    
    Args:
        arg1: Describe the arguments of the function
    
    Keyword Args:
        kwarg1: Describe keyword arguments of function (defaultvalue)

    Returns:
        Describe the type and content of what the function returns here.
        It can be useful to give an example if the type is complicated.
    
    Raises:
        If any exceptions can be raised by the function, describe them.
    """
    
    # Function body here - note the nice extra indented line for whitespace
    
    # The "return" keyword specifies the output of the function
    return output
