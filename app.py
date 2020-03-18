from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    g=12
    s=14

    print(g+s)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
