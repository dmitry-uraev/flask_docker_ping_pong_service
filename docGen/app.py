import requests

from flask import Flask, request, render_template
from generator import simple_doc_converter, save_file


app = Flask(__name__)


@app.route('/')
def start_root():
    return render_template('index.html')


@app.route('/docParse', methods=['GET'])
def send_url_docparse():
    if request.method == 'GET':
        url_to_parse = request.args.get('url')
        if url_to_parse is not None:
            if url_to_parse != 'None':
                if url_to_parse[:4] == 'http':
                    response = requests.get(
                        'http://docparse-container:5001/parse_text',
                        {
                            'url': url_to_parse
                        }
                    )
                    save_file(response.text)
                    return "Done. File is saved locally."
    return render_template('get_text.html')


@app.route('/get_text')
def send_url():
    try:
        response = requests.get('http://docparse-container:5001/get_parsed_text').text
        return simple_doc_converter(response)
    except requests.exceptions.RequestException as e:
        print('Cannot reach the parser service. \n')
        return 'End. \n'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
