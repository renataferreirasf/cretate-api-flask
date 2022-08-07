from crypt import methods
from flask import Flask

app = Flask("Nana")

@app.route("/nana", methods=["GET"])
def hello_world():
    return "Hello, World!"

app.run()