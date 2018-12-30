# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 21:39:08 2018

@author: acvid
"""

from flask import Flask
import mymodule   # just playing along

app = Flask( __name__ ) # creat an object named after active pkg

@app.route('/')     # a decorator? => trigger function defined just below
def home() -> 'html':
    return "I am alive!"

app.run()
