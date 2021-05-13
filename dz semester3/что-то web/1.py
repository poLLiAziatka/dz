from flask import Flask

app = Flask(name)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


if name == 'main':
    app.run(port=8080, host='127.0.0.1')