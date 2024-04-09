#!/usr/bin/env python3
"""app flask Module"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """class Config for translation"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def home() -> str:
    """home route for app application"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
