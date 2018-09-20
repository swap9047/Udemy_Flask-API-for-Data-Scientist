#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 12:34:08 2018

@author: swap9047
"""

from flask import Flask,request
app=Flask(__name__)

@app.route('/',methods=['POST'])
def add():
    a=request.form['a']
    b=request.form['b']
    return str(int(a)+int(b))

if __name__=='__main__':
    app.run(port=7000)
