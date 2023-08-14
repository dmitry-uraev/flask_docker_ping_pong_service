import sys
import re
import requests
from flask import Flask, render_template, request
from parser import parse_website

app = Flask(__name__)
URL = "https://www.docker.com"


@app.route('/')
def start_root():
    return render_template("index.html")


@app.route('/parse_text', methods=['GET'])
def parse_text():
    return parse_website(request.args.get('url'))


@app.route('/get_parsed_text', methods=['GET'])
def parse_website_response():
    try:
        url_to_parse = request.args.get('url')
        if url_to_parse is not None or url_to_parse != 'None':
            return ' '.join(re.findall(r'\w+', parse_website(url_to_parse)))
    except requests.exceptions.MissingSchema:
        return render_template('parse_text.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
