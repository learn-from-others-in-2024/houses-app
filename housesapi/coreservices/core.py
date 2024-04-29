from flask import Flask


core = Flask(__name__)


@core.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    core.run(host='0.0.0.0', port=5000, debug=True)
