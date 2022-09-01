import werkzeug
from flask import Flask, request
from morseDictionary import MorseDictionary, morseconverter

app = Flask(__name__)


@app.route("/")
def hello():
    return MorseDictionary


@app.route("/convert/")
def convert():
    string = request.args.get('text')
    response = {"result": {
        "original": string,
        "morse": morseconverter(string)
    }}
    return response


if __name__ == "__main__":
    app.run()
