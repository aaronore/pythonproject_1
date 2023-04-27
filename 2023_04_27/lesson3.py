from flask import Flask,request,make_response
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    message = "<h1>request headers</h1>"
    message += f"<ul><li>host:{request.headers.get('Host')}</li>"
    message += f"<li>host_url:{request.headers.get('host_url')}</li>"
    message += f"<li>user_agent:{request.headers.get('User-Agent')}</li>"
    message +=  f"<li>Accept-Language:{request.headers.get('Accept-Language')}</li></ul>"
    return message

@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello!{name}</h1>"

@app.route("/error")
def error():
    return "<h1>error</h1>",404

@app.route("/oreo")
def oreo():
    return render_template("index.html")