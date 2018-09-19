#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Benjamin Seeley
# Student ID: 2262810
# Email: seele105@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW03
###

def main(local_argv):
    import sequences
    print(sequences.fibonacci(int(local_argv[1]))[-1])

if __name__ == "__main__":
    import sys
    main(sys.argv)