from flask import Flask

app=Flask(__name__)

@app.route("/hello")
def print_hello():
    return "Hello From Cookie!!!"

app.run(host='0.0.0.0',port=5000)