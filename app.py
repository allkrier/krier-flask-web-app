# module 11 - Flask Application
# Mike Colbert 4/06/2025

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!!"


@app.route("/allie")
def allie():
    x = 12
    y = 16
    z = x + y
    name = "Allie"
    return f"Hello {name}, the sum of {x} and {y} is {z}!!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
