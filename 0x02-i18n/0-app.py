#!/usr/bin/env python3
"""app flask Module"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home() -> str:
    """home route for app application"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
