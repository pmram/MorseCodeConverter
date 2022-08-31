from flask import Flask
from morseDictionary import MorseDictionary

app = Flask(__name__)


@app.route("/")
def hello():
    return MorseDictionary


if __name__ == "__main__":
    app.run()