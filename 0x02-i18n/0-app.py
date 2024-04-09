#!/usr/bin/env python3
"""app flask Module"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home()-> str:
    """home route for app application"""
    title = 'Welcome to Holberton'
    h1 = 'Hello world'
    return render_template('index.html', title=title, h1=h1)


if __name__ == "__main__":
    app.run()
