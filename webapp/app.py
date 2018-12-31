# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 21:39:08 2018

@author: acvid
"""

from flask import Flask, render_template, request
import mymodule   # just playing along

app = Flask( __name__ ) # creat an object named after active pkg

@app.route('/')     # a decorator? => trigger function defined just below
def home() -> 'html':
    return render_template('entry.html', page_title='Play with functions')

@app.route('/findcommonletters', methods=['POST'])
def findcommonletters() -> 'html':
    results = mymodule.find_common_letters( request.form['sentence'], request.form['letters'])
    return render_template('results.html', results_title='Common Letters:', the_results=results)

@app.route('/countvowels', methods=['POST'])
def countvowels() -> 'html':
    results = mymodule.count_vowels( request.form['sentence'] )
    return render_template('results.html', results_title='Vowels:', the_results=results)

app.run()
