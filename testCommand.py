import subprocess

from flask import Flask, render_template
app = Flask(__name__)

def run_command(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/')
def index():
    return render_template('index.html')
    #return "index yoyoyo"

@app.route('/<command>')
def command_server(command):
    return run_command(command)

if __name__ == '__main__':
    app.run(debug=True, port=99, host='0.0.0.0')
