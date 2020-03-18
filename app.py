from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    g=12
    print(g)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
