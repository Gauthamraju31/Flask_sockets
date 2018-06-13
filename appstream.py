from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return "HELLO"
    return render_template('cam_check.html')


if __name__ == '__main__':
    app.run(host='192.168.0.6', threaded=True)
    # app.run(host='localhost', threaded=True)
