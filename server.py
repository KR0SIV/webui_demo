from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/echo", methods=['POST'])
def echo():
    command = request.form['text']
    subprocess.call([command])
    #return request.form['text'] + " Command executed via subprocess"
    return index()

@app.route("/calc", methods=['POST'])
def calc():
    subprocess.call('calc.exe')
    return index()

@app.route("/test", methods=['POST'])
def test():
    while True:
        subprocess.call('calc.exe')

if __name__ == "__main__":
    app.run(debug='True')