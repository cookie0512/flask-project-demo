from flask import Flask

app=Flask(__name__)

@app.route("/hello")
def print_hello():
    return "Hello From Cookie~!~!"

@app.route("/pick-up-lines")
def pick_up_lines():
    return """
        I love you once,
        I love you twice,
        I love you more than beans and rice.
    """

app.run(host='0.0.0.0',port=5000)