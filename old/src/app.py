from flask import flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

if __name__ == '__main__':
    app.run(port=4888)
