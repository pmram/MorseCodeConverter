from flask import Flask, request, jsonify
from errorHandling import InvalidUsage
from morseDictionary import MorseDictionary, morse_converter

app = Flask(__name__)


@app.route("/")
def hello():
    return MorseDictionary


@app.route("/convert")
def get_morse_code():
    string = request.args.get('text')
    separator = request.args.get('separator')
    error_char = request.args.get('error_char')
    if string is None:
        raise InvalidUsage('Missing parameter', status_code=400)
    response = {"result": {
        "original": string,
        "morse": morse_converter(string, separator, error_char)
    }}
    return response


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == "__main__":
    app.run()
