import requests
from flask import Flask, Response, jsonify

app = Flask(__name__)

@app.route('/json')
def test_json() -> Response:
    """Returns a test remote JSON payload"""
    response = requests.get('https://httpbin.org/json')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=8000)