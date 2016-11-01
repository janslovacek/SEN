from bottle import route, run, template, debug, static_file
import bottle
import os
from core import database_module


class Paths(object):
    ROOT = os.path.dirname(__file__)
    TEMPLATES = ROOT + "/templates/"
    STATIC_FILES = ROOT + "/static/"


@route('/')
@route('/home')
def home():
    return template('home.tpl')


@route('/weather')
def weather():
    return template('weather.tpl')


@route('/stats')
def stats():
    return template('stats.tpl')


@route('/records')
def records():
    db = database_module.DatabaseModule()
    items = db.get_records()
    print(items)
    return template('database.tpl', records=items)


@route('/static/<file_path:path>')
def server_static(file_path):
    return static_file(file_path, root=Paths.STATIC_FILES)


def run_server():
    bottle.TEMPLATE_PATH.append(Paths.TEMPLATES)
    debug(True)
    run(host='0.0.0.0', port=8080, reloader=True, server='waitress')

