from flask import Flask, request, jsonify
from errorHandling import InvalidUsage
from morseDictionary import MorseDictionary, morseconverter

app = Flask(__name__)


@app.route("/")
def hello():
    return MorseDictionary


@app.route("/convert/")
def convert():
    string = request.args.get('text')
    if string is None:
        raise InvalidUsage('This view is gone', status_code=410)
    response = {"result": {
        "original": string,
        "morse": morseconverter(string)
    }}
    return response


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == "__main__":
    app.run()
