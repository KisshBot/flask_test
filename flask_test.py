# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:33:10 2019

@author: _KK_
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hey ShunyEka Systems!"

if __name__ == "__main__":
    app.run()