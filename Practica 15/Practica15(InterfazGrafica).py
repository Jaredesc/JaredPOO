from flask import Flask, request, abort

app = Flask(__name__)

ALLOWED_IP = '10.2.80.57'

@app.before_request
def limit_remote_addr():
    if request.remote_addr != ALLOWED_IP:
        abort(403) 

@app.route('/')
def hello_world():
    return "Hola Mundo"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)