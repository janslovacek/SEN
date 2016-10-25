from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

def run_server():
    run(host='0.0.0.0', port=8080)
