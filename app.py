from flask import Flask

app=Flask(__name__)

@app.route("/hello")
def print_hello():
    return "Hello From Cookie~!~!"

@app.route("/pickup-lines")
def pick_up_lines():
    return """
        I love you once,\n
        I love you twice,\n
        I love you more than beans and rice.\n
    """

app.run(host='0.0.0.0',port=5000)