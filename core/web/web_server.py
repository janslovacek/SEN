from bottle import route, run, template, debug, static_file
import bottle
import os
import database_module
from helper import IO


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
    db = database_module.DatabaseModule()
    current_weather = db.get_last_record()[0]
    return template('weather.tpl', record=current_weather)


@route('/stats')
def stats():
    return template('stats.tpl')


@route('/records')
def records():
    db = database_module.DatabaseModule()
    items = db.get_records()
    print(items)
    return template('database.tpl', records=items)


@route('/json')
def json():
    db = database_module.DatabaseModule()
    items = db.get_records()
    chart_json = IO.records_to_chart_json(items)
    return chart_json


@route('/rgbw_json')
def json():
    db = database_module.DatabaseModule()
    items = db.get_records()
    chart_json = IO.rgbw_to_json(items)
    return chart_json


@route('/static/<file_path:path>')
def server_static(file_path):
    return static_file(file_path, root=Paths.STATIC_FILES)


def run_server():
    bottle.TEMPLATE_PATH.append(Paths.TEMPLATES)
    debug(True)
    run(host='0.0.0.0', port=8080, reloader=True, server='waitress')

