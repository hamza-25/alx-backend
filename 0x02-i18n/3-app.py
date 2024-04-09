#!/usr/bin/env python3
"""app flask Module"""
from flask import Flask, render_template, request
from flask_babel import Babel # type: ignore
from typing import Any


class Config:
    """class Config for translation"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Any:
    """return best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> str:
    """home route for app application"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
