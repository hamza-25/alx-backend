#!/usr/bin/env python3
"""app flask Module"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union
import pytz


class Config:
    """class Config for translation"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)
app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """get user from query pram"""
    id = request.args.get('login_as')
    if id:
        return users.get(int(id))
    return None


@app.before_request
def before_request() -> None:
    """before_reques assign user globaly"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """return best match with our supported languages"""
    locale = request.args.get('locale', '')
    if locale:
        return locale
    if g.user and g.user.get('locale', '') in app.config['LANGUAGES']:
        return g.user.get('locale', '')
    header = request.headers.get('locale', '')
    if header:
        return header
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    """set time zone with level"""
    timezone = request.args.get('timezone', '')
    try:
        if timezone and pytz.timezone(timezone):
            return timezone
        user_timezone = g.user.get('timezone', '')
        if g.user and user_timezone and pytz.timezone(user_timezone):
            return g.user.get('timezone', '')
    except pytz.exceptions.UnknownTimeZoneError as e:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def home() -> str:
    """home route for app application"""
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
