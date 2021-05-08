#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     bext_demo1.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue # 169
# Written by G.D. Walters
# Copyright (c) 2021 by G.D. Walters
# This source code is released under the MIT License
# ======================================================

try:
    import bext
except ImportError:
    print(
        "This program requires the use of the Bext library.  Please install it into your Python"
    )
    print('installation by using "pip install bext".')

# get the width and height of the current terminal
bext.bg("black")
bext.fg("green")
bext.clear()
width, height = bext.size()
print(f"Terminal width: {width}  height: {height}")

# bext.clear()
bext.goto(0, 1)
print("This is a test.")
bext.goto(10, 6)
print("This is a test at 10,6")
bext.goto(0, height - 1)
