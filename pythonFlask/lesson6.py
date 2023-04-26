from flask import Flask

app = Flask(__name__)   #整個應用程式的跟目錄

@app.route("/")  #decorator提供一個function給他  
def abc():
    return "<h1>Hello! Flask!</h1>"