#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     Bext_test1.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue #169
# Written by G.D. Walters
# Copyright (c) 2021 by G.D. Walters
# This source code is released under the MIT License
# ======================================================

import bext

# Center a string on a particular terminal line
def centre(str, line):
    leng = len(str)
    wid, hei = bext.size()
    xpos = wid / 2 - leng / 2
    bext.goto(xpos, line)
    print(str)


# Set basic parameters
def SetUpScreen(inverted):
    global width, height
    background = "black"
    foreground = "green"
    bext.title = "Bext Test 1"
    if inverted == False:
        bext.fg(foreground)
        bext.bg(background)
    else:
        bext.fg(background)
        bext.bg(foreground)
    width, height = bext.size()


# Define the prompts, text and positions for inputs
def Setup():
    global prompts, texts, entryPos
    prompts = [(0, 2), (40, 2), (0, 3), (0, 4), (30, 4), (50, 4)]
    texts = [
        "First Name: ",
        "Last Name: ",
        "Address: ",
        "City: ",
        "State: ",
        "Postal Code: ",
    ]
    entryPos = [(12, 2), (51, 2), (9, 3), (6, 4), (37, 4), (63, 4)]


# Creates the screen "form"
def FillScreen():
    global prompts, texts, entryPos
    bext.goto(prompts[0][0], prompts[0][1])
    print(texts[0])
    bext.goto(prompts[1][0], prompts[1][1])
    print(texts[1])
    bext.goto(prompts[2][0], prompts[2][1])
    print(texts[2])
    bext.goto(prompts[3][0], prompts[3][1])
    print(texts[3])
    bext.goto(prompts[4][0], prompts[4][1])
    print(texts[4])
    bext.goto(prompts[5][0], prompts[5][1])
    print(texts[5])


# Code to get the various inputs from screen "form"
def GetEntry():
    global prompts, texts, entryPos
    bext.goto(entryPos[0][0], prompts[0][1])
    fn = input()
    bext.goto(entryPos[1][0], prompts[1][1])
    ln = input()
    bext.goto(entryPos[2][0], prompts[2][1])
    addr = input()
    bext.goto(entryPos[3][0], prompts[3][1])
    city = input()
    bext.goto(entryPos[4][0], prompts[4][1])
    state = input()
    bext.goto(entryPos[5][0], prompts[5][1])
    postal = input()


global width, height
SetUpScreen(False)
Setup()
bext.clear()
centre("Welcome to old time data entry", 0)
FillScreen()
SetUpScreen(True)
GetEntry()
bext.goto(0, height - 1)
print("Entry is done.  Thank you!")
